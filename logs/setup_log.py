import logging

log = logging.getLogger()
log.setLevel(logging.DEBUG)

formatter=logging.Formatter("%(asctime)s|%(name)s|%(message)s")
handler=logging.FileHandler("logs/apps.log")

handler.setFormatter(formatter)
log.addHandler(handler)