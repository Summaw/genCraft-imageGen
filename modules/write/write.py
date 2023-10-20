import sys, colr, time

def write(text: str, case: str) -> None:
    current_time = time.strftime("%H:%M:%S", time.localtime())
    switcher = {
        'info': _write_info,
        'success': _write_success,
        'error': _write_error
    }
    func = switcher.get(case.lower(), lambda x, y: None)
    func(current_time, text)

def _write_info(current_time, text):
    sys.stdout.write(f"[{colr.Colr().hex('#525052', current_time)}] {colr.Colr().hex('#00008B', '[INFO]')} {colr.Colr().hex('#Eceeee', text)}\n")
    sys.stdout.flush()

def _write_success(current_time, text):
    sys.stdout.write(f"[{colr.Colr().hex('#525052', current_time)}] {colr.Colr().hex('#47f566', '[SUCCESS]')} {colr.Colr().hex('#Eceeee', text)}\n")
    sys.stdout.flush()

def _write_error(current_time, text):
    sys.stdout.write(f"[{colr.Colr().hex('#525052', current_time)}] {colr.Colr().hex('#F55947', '[ERROR]')} {colr.Colr().hex('#Eceeee', text)}\n")
    sys.stdout.flush()