import sys
import os

# ensure imports work
sys.path.insert(0, os.path.join(os.getcwd(), 'PyShooter'))

import timer


def make_time_func(values):
    vals = list(values)
    last = vals[-1]
    def f():
        if vals:
            return vals.pop(0)
        return last
    return f


def test_timer_triggers_action_once(monkeypatch):
    # arrange: fake time sequence (seconds)
    monkeypatch.setattr(timer.time, 'time', make_time_func([0.0, 0.5, 1.6]))
    called = []
    t = timer.Timer()
    t.duration = 1000  # milliseconds
    t.action = lambda: called.append('done')

    # act: two updates
    t.update()  # ~500ms passed -> not yet
    assert called == []
    t.update()  # additional ~1100ms -> triggers

    # assert
    assert called == ['done']
    assert t.done is True


def test_repeate_timer_calls_multiple_times(monkeypatch):
    # three trigger events expected
    monkeypatch.setattr(timer.time, 'time', make_time_func([0.0, 1.1, 2.3, 3.5]))
    calls = []
    rt = timer.RepeateTimer()
    rt.duration = 1000
    rt.action = lambda: calls.append('x')

    rt.update()  # ~1.1s -> triggers first
    rt.update()  # ~1.2s -> triggers second
    rt.update()  # ~1.2s -> triggers third

    assert len(calls) == 3
    assert rt.done is False


def test_repeate_n_timer_stops_after_n(monkeypatch):
    monkeypatch.setattr(timer.time, 'time', make_time_func([0.0, 1.2, 2.5, 3.8]))
    calls = []
    rtn = timer.RepeateNTimer()
    rtn.duration = 1000
    rtn.ntimes = 2
    rtn.action = lambda: calls.append('n')

    rtn.update()  # trigger 1
    rtn.update()  # trigger 2 -> should cancel after this
    rtn.update()  # should have no effect

    assert len(calls) == 2
    assert rtn.executions == 2
    assert rtn.done is True
