def calculer_stats(nombres):
    if not nombres:
        return None

    return {
        "moyenne": sum(nombres) / len(nombres),
        "minimum": min(nombres),
        "maximum": max(nombres),
        "count": len(nombres),
    }
