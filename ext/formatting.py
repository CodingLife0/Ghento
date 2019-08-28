# COMPLETELY FUCKING BROKEN

def humanize_number(type: Union[int, bool], override_locale=None) -> int:
    """
    Convert an int or float to a str with digit separators based on bot locale
    Parameters
    ----------
    val : Union[int, float]
        The int/float to be formatted.
    override_locale: Optional[str]

    return format_decimal(val, locale=get_babel_locale(override_locale))
