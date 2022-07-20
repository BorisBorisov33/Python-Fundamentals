def is_winning(ticket):
    if len(ticket) != 20:
        return "invalid ticket"

    left_side = ticket[:10]
    right_side = ticket[10:]
    # print(left_side, right_side)
    winning_symbols = ['@', '#', '$', '^']
    for winning_symbol in winning_symbols:
        for repetition in range(10, 5, -1):
            winning_symbol_repetition = winning_symbol * repetition
            if winning_symbol_repetition in left_side and winning_symbol_repetition in right_side:
                if repetition == 10:
                    return f'ticket "{ticket}" - {repetition}{winning_symbol} Jackpot!'
                return f'ticket "{ticket}" - {repetition}{winning_symbol}'
            # print(winning_symbol_repetition)
    return f'ticket "{ticket}" - no match'


tickets = [ticket.strip() for ticket in input().split(', ')]
for ticket in tickets:
    print(is_winning(ticket))
