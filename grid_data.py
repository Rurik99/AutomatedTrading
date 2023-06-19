orders_count = 5  # по 5 ордеров с каждой стороны: 5 на лонг, 5 на шорт, плюс два стопа


grid = {
    "BTCUSDT": [28_000, 29_000],
    "ETHUSDT": [2100, 2500],
    "ADAUSDT": [60, 70],
}


def get_grid(coin):
    grid_start = grid[coin][0]
    grid_stop = grid[coin][1]
    differ = grid_stop - grid_start
    half_path_differ = differ / 2

    differ_step = half_path_differ / orders_count
    buy_grid = []
    sell_grid = []
    for i in range(orders_count):
        buy_grid.append(grid_start + differ_step * i)
        sell_grid.append(grid_stop - differ_step * i)
    return buy_grid, sell_grid
    
