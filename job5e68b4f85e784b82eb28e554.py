import traceback
import sys
from operations import TopOperation
from operations import JoinOperation
from operations import AggregationOperation
from operations import FormulaOperation
from operations import FilterOperation
from connectors import DBFSConnector
from connectors import CosmosDBConnector
from datatransformations import TranformationsMainFlow
from automl import tpot_execution
from core import PipelineNotification
import json

try: 
	PipelineNotification.PipelineNotification().started_notification('5e68b4f85e784b82eb28e555','5df78f4be2f2eff24740bbd7','http://13.68.212.36:3200/pipeline/notify')
	TestAPP_DBFS = DBFSConnector.DBFSConnector.fetch([], {}, "5e68b4f85e784b82eb28e555", spark, "{'url': '/Demo/MovieRatingsTrain.csv', 'file_type': 'Delimeted', 'dbfs_token': 'dapi0ef076722999cf4cd8859e9aafdb7b76', 'dbfs_domain': 'westus.azuredatabricks.net', 'delimiter': ',', 'is_header': 'Use Header Line'}")

	PipelineNotification.PipelineNotification().completed_notification('5e68b4f85e784b82eb28e555','5df78f4be2f2eff24740bbd7','http://13.68.212.36:3200/pipeline/notify')
except Exception as ex: 
	PipelineNotification.PipelineNotification().failed_notification(ex,'5e68b4f85e784b82eb28e555','5df78f4be2f2eff24740bbd7','http://13.68.212.36:3200/pipeline/notify','http://13.68.212.36:3200/logs/getProductLogs')
	sys.exit(1)
try: 
	PipelineNotification.PipelineNotification().started_notification('5e68b4f85e784b82eb28e556','5df78f4be2f2eff24740bbd7','http://13.68.212.36:3200/pipeline/notify')
	TestAPP_AutoFE = TranformationsMainFlow.TramformationMain.run(["5e68b4f85e784b82eb28e555"],{"5e68b4f85e784b82eb28e555": TestAPP_DBFS}, "5e68b4f85e784b82eb28e556", spark,json.dumps( {"FE": [{"feature": "UserId", "transformation": "", "type": "numeric", "replaceby": "mean", "selected": "True", "stats": {"count": "2587", "mean": "465.06", "stddev": "264.69", "min": "1", "max": "943", "missing": "0"}}, {"feature": "MovieId", "transformation": "", "type": "numeric", "replaceby": "mean", "selected": "True", "stats": {"count": "2587", "mean": "432.85", "stddev": "337.75", "min": "1", "max": "1656", "missing": "0"}}, {"feature": "Rating", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "2587", "mean": "3.52", "stddev": "1.15", "min": "1.0", "max": "5.0", "missing": "0"}, "transformation": ""}, {"transformationsData": {"feature_label": "Timestamp"}, "feature": "Timestamp", "type": "date", "selected": "True", "replaceby": "random", "stats": {"count": "", "mean": "", "stddev": "", "min": "", "max": "", "missing": "0"}, "transformation": "Extract Date"}, {"feature": "AvgRating", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "2587", "mean": "3.53", "stddev": "0.44", "min": "1.51", "max": "4.67", "missing": "0"}, "transformation": ""}, {"feature": "Timestamp_dayofmonth", "transformation": "", "type": "numeric", "generated": "True", "selected": "True", "stats": {"count": "2587", "mean": "16.05", "stddev": "9.06", "min": "1", "max": "31", "missing": "0"}}, {"feature": "Timestamp_month", "transformation": "", "type": "numeric", "generated": "True", "selected": "True", "stats": {"count": "2587", "mean": "7.0", "stddev": "4.34", "min": "1", "max": "12", "missing": "0"}}, {"feature": "Timestamp_year", "transformation": "", "type": "numeric", "generated": "True", "selected": "True", "stats": {"count": "2587", "mean": "1997.45", "stddev": "0.5", "min": "1997", "max": "1998", "missing": "0"}}]}))

	PipelineNotification.PipelineNotification().completed_notification('5e68b4f85e784b82eb28e556','5df78f4be2f2eff24740bbd7','http://13.68.212.36:3200/pipeline/notify')
except Exception as ex: 
	PipelineNotification.PipelineNotification().failed_notification(ex,'5e68b4f85e784b82eb28e556','5df78f4be2f2eff24740bbd7','http://13.68.212.36:3200/pipeline/notify','http://13.68.212.36:3200/logs/getProductLogs')
	sys.exit(1)
try: 
	PipelineNotification.PipelineNotification().started_notification('5e68b4f85e784b82eb28e557','5df78f4be2f2eff24740bbd7','http://13.68.212.36:3200/pipeline/notify')
	TestAPP_AutoML = tpot_execution.Tpot_execution.run(["5e68b4f85e784b82eb28e556"],{"5e68b4f85e784b82eb28e556": TestAPP_AutoFE}, "5e68b4f85e784b82eb28e557", spark,json.dumps( {"model_type": "regression", "label": "AvgRating", "features": ["UserId", "MovieId", "Rating", "Timestamp", "Timestamp_dayofmonth", "Timestamp_month", "Timestamp_year"], "percentage": "10", "executionTime": "5", "sampling": "0", "sampling_value": "", "run_id": "", "model_id": "5e68b7a95e784b82eb28e572", "ProjectName": "ML Sample Problems", "PipelineName": "TestAPP", "pipelineId": "5e68b4f85e784b82eb28e554", "userid": "5df78f4be2f2eff24740bbd7", "runid": "", "url_ResultView": "http://13.68.212.36:3200", "experiment_id": "480623611921769"}))

	PipelineNotification.PipelineNotification().completed_notification('5e68b4f85e784b82eb28e557','5df78f4be2f2eff24740bbd7','http://13.68.212.36:3200/pipeline/notify')
except Exception as ex: 
	PipelineNotification.PipelineNotification().failed_notification(ex,'5e68b4f85e784b82eb28e557','5df78f4be2f2eff24740bbd7','http://13.68.212.36:3200/pipeline/notify','http://13.68.212.36:3200/logs/getProductLogs')
	sys.exit(1)

