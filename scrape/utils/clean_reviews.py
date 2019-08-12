from scrape.models import Yelp, Results
import datetime
from datetime import timedelta
import logging

logger = logging.getLogger(__name__)

time_threshold = datetime.datetime.now() - timedelta(hours=3)
objects = Yelp.objects.filter(scrape_date__lt=time_threshold)

for obj in objects:
    if obj:
        records_removed = objects.delete()
        logger.info(str(records_removed[1]['scrape.Yelp']) + ' Yelp record(s) and ' + str(records_removed[1]['scrape.Results']) + ' associated reviews have been successfully deleted.')
    else:
        pass
