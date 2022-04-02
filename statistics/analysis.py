import statistics.central_tendency as central_tendency
import statistics.dispersion as dispersion


def get_full_analysis(x: list[float]) -> None:
    # Central Tendency
    mean = central_tendency.mean(x)
    mode = central_tendency.mode(x)
    median = central_tendency.median(x)

    # Dispersion
    range_ = dispersion.range_(x)
    variance = dispersion.variance(x)
    standard_deviation = dispersion.standard_deviation(x)

    # Show results
    print(
        f"""
Central Tendency:
 - mean:\t{mean}
 - mode:\t{mode}
 - median:\t{median}

Dispersion:
 - range:\t{range_}
 - variance:\t{variance}
 - standard deviation:\t{standard_deviation}
    """
    )
