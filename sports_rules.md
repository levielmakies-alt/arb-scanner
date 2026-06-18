# Sports Arb Scanner Rules

Goal: Find risk-free sports arbitrage between Polymarket and Kalshi.

Start with:
- NBA winner markets
- NFL winner markets
- MLB winner markets

Avoid for now:
- Soccer
- Player props
- Over/unders
- Point spreads
- Complicated futures

Formula:
Polymarket Team A YES + Kalshi Team A NO <= 0.96

or

Polymarket Team A NO + Kalshi Team A YES <= 0.96

Minimum gross edge:
4%

Only match markets if:
- Same sport
- Same teams
- Same game date
- Same exact outcome