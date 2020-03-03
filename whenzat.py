import pendulum
import json
import typing

def loader(json_: str='when.json', from_file: bool=True):
    """Return a list of datetimes for the requested json file"""

    if from_file:
        return json.load(json_)

    else:
        return json.loads(json_)


def pick_date(date: list, start=None):
    """
    iterate through list of ints or str formatted dates and return the optimal
    date.
    """

    is_string = all([is_instance(x, str) for x in date])
    is_int = all([is_instance(x, int) for x in date])

    if all([is_string, is_int]) or None([is_string, is_int]):
        raise(
            ValueError('Please provide one type of \
                date type (either ints or str'),
        )

    if not start:
        starting_date = pendulum.now()

    else:
        starting_date = pendulum.parse(start, strict=False)

    if is_string:
        dates = [pendulum.parse(d, strict=False) for d in date]

    if is_int:
        dates = [parse_int(d) for d in date]

    return max(dates)


def parse_int(date: int):
    """
    Get the period between the target date and the starting_date. Use when
    the date is an int.
    """
    target = pendulum.now()
    target = target.set(day=date).set(tz=pendulum.local_timezone())
    return target
