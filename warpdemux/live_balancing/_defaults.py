DEFAULT_MODEL_NAME = "WDX12"

DEFAULT_MIN_CHANNEL = 1

DEFAULT_MAX_MISSED_START_OFFSET = 400
DEFAULT_MAX_CHUNK_SIZE = 15000
DEFAULT_MIN_CHUNK_SIZE = 2500

DEFAULT_BALANCE_THRESHOLD = 0.05
DEFAULT_MIN_STAT = 100
DEFAULT_PRED_CONF_THRESHOLD = 0.2
DEFAULT_BALANCE_TYPE = "adapter_count"
DEFAULT_CHANNEL_FRAC = 1
DEFAULT_POD5_CHECK_INTERVAL = 1

DEFAULT_SAVE_EVERY_SEC = 30

DEFAULT_NPROC_SEGMENTATION = 2
DEFAULT_NPROC_CLASSIFICATION = 4

DEFAULT_REJECT_DURATION = 0.1
DEAFULT_REPEATED_UNBLOCK_TIME_WINDOW = 1.5
DEFAULT_REPEATED_UNBLOCK_DURATION_2 = 0.5
DEFAULT_REPEATED_UNBLOCK_DURATION_3 = (
    2.0  # should be more than DEAFULT_REPEATED_UNBLOCK_TIME_WINDOW
)

DEFAULT_WATCH_FOR_MISSING = True
DEFAULT_WAIT_TO_SEE = 900  # in seconds; 15 minutes (first 4 are pore scanning)
DEFAULT_MAX_SIGNAL_AFTER_POLYA = 1500