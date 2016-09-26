from datetime import timedelta, datetime
import pandas as pd

from instore.models import Sensor

from .metric import Metric
from .metric_definitions import SENSOR_TYPE_METRICS


class CliShot(object):
    """
    CliShot is a definition for:
    metric + location + provider + dates + sensor(s)

    :param location: Location instance
    :param provider: Provider instance
    :param dates: Tuple or list of date objects containing initial and final
        dates to query for.
    :param sensor_type: Type of sensors that will be considered. This
        parameter is used to generate the metric.
    :param sensors: sensor/ist containing sensors to query for

    TODO: Use a namedtuple for dates
          Implement sensor(s) parser
    """
    def __init__(self, location, provider, dates, sensor_type=None,
                 sensors=None):
        self.location = location
        self.provider = provider
        self.dates = dates
        self.sensor_type = sensor_type
        if not sensor_type and not sensors:
            raise ValueError('''Either sensor_type or sensors must not be
                             None''')
        self.sensors = sensors or self.get_sensors()
        self.metric = self.generate_metric()

    def get_sensors(self):
        if self.sensor_type:
            return [sensor for sensor in Sensor.select().where(
                (Sensor.provider == self.provider.id) &
                (Sensor.sensor_type == self.sensor_type))]
        return None

    def dates_to_list(self):
        """
        Return a list of days for which CliShot will get/process/export
        data.
        """
        dates_list = list()
        day = datetime.strptime(self.dates['date_from'], '%Y-%m-%d')
        while day <= datetime.strptime(self.dates['date_to'], '%Y-%m-%d'):
            dates_list.append(day)
            day += timedelta(days=1)
        return dates_list

    def generate_metric(self):
        """
        Generate a metric attribute of type clinstore.metric.Metric

        TODO: use new Metric class.
        """
        if self.sensor_type:
            metric_name = SENSOR_TYPE_METRICS[self.provider.alias][
                self.sensor_type]
            return Metric(metric_name, self.provider)
        else:
            return None

    def get_data(self, **kwargs):
        """
        Obtain data by calling the provider.get_data function in a
        daily basis for the date range specified in self.dates.
        """
        dates = self.dates_to_list()
        data = pd.DataFrame()
        if self.sensor_type:
            for day in dates:
                for sensor in self.sensors:
                    buff = self.provider.get_data(dates=(day, day),
                                                  sensor_id=sensor.sensor_id,
                                                  dtype=sensor.sensor_type)
                    if data.empty:
                        data = self.parse(buff, day=day)
                    else:
                        data = data.append(self.parse(buff, day=day))
        else:
            # TODO: Manage obtaining data from a list of sensors that can
            # belong to different metrics.
            pass
        return data

    def parse(self, df, **kwargs):
        if self.metric:
            return self.metric.parse(df, **kwargs)
        # TODO: Raise an exception

    def process(self, df):
        if self.metric:
            return self.metric.process(self.location, self.provider, df)
        # TODO: Raise an exception

    def export(self, df):
        if self.metric:
            return self.metric.export(self.location, self.provider,
                                      self.dates, df)
        # TODO: Raise an exception
