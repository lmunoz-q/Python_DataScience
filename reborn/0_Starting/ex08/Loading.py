def ft_tqdm(lst: range) -> None:
    total = len(lst)
    bar_lenght = 65
    for i, elem in enumerate(lst, start=1):
        percent = (i / total) * 100
        filled_lenght = int(bar_lenght * i // total)
        bar = '█' * filled_lenght + ' ' * (bar_lenght - filled_lenght)
        print(
            f"\r{percent:3.0f}%|{bar}| {i}/{total} ({percent:.1f}%)",
            end='', flush=True
        )

        yield elem

    print()
