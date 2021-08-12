class GPS:
    '''
    GPS座標のクラス
    '''

    def __init__(self, lat: float = 34.4908711, lon: float = 136.6874736, max_lat: float = None, min_lat: float = None, max_lon: float = None, min_lon: float = None):
        self.__lat = lat
        self.__lon = lon

        self.__max_lat = max_lat
        self.__min_lat = min_lat
        self.__max_lon = max_lon
        self.__min_lon = min_lon

        return

    def add(self, lat: float, lon: float):
        self.__lat += lat
        self.__lon += lon

        self._validate()

        return

    @property
    def lat(self):
        '''
        緯度
        '''

        return self.__lat

    @property
    def lon(self):
        '''
        経度
        '''

        return self.__lon

    def _validate(self):
        '''
        座標の最大・最小値を超えないように検証し、問題があれば調節する
        '''

        # 緯度が最大値を超える場合
        if type(self.__max_lat) is float and self.__lat > self.__max_lat:
            self.__lat = self.__max_lat
            pass

        # 緯度が最小値を超える場合
        if type(self.__min_lat) is float and self.__lat < self.__min_lat:
            self.__lat = self.__min_lat
            pass

        # 経度が最大値を超える場合
        if type(self.__max_lon) is float and self.__lon > self.__max_lon:
            self.__lon = self.__max_lon
            pass

        # 経度が最小値を超える場合
        if type(self.__min_lon) is float and self.__lon < self.__min_lon:
            self.__lon = self.__min_lon
            pass

        return
