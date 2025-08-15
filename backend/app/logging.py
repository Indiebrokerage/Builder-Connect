import logging, sys
def configure_logging(level=logging.INFO):
    handler = logging.StreamHandler(sys.stdout)
    fmt = logging.Formatter('%(asctime)s %(levelname)s %(name)s %(message)s')
    root = logging.getLogger()
    root.setLevel(level); handler.setFormatter(fmt); root.addHandler(handler); return root
