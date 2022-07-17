import pytest
from pageObjects.AddWatchlist import Watchlist
from utilities.customLogger import LogGen


class Test001WatchlistAdd:
    logger = LogGen.loggen()

    @pytest.mark.regression
    @pytest.mark.uat
    @pytest.mark.usefixtures("base_fixture")
    def test_watchlist_add(self, setup):
        self.logger.info("****************** Test001WatchlistAdd/test_watchlist_add is started ******************")
        self.wl = Watchlist(setup)
        self.wl.add_film_to_wl()
        self.wl.wl_btn_main()
        self.wl.check_film_in_wl()
        self.logger.info("************** Test001WatchlistAdd/test_watchlist_add is completed ************")
