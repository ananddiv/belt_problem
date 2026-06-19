# Belt Production Optimization — Linear Programming Problem

## Problem Statement

A factory produces two types of belts, **Belt A** and **Belt B**. The factory wants to determine the optimal daily production quantities to maximize total profit, subject to constraints on production time, leather availability, and buckle availability.

### Profit per Unit

| Belt | Profit |
|------|--------|
| Belt A | $3 |
| Belt B | $4 |

### Production Time Constraint

Belt A takes **twice as long** to produce as Belt B. If the factory dedicated all its time to producing Belt B alone, it could produce **1,000 units** per day. So, in terms of "Belt B equivalent" time, one unit of Belt A consumes as much production time as two units of Belt B.

### Leather Constraint

Both belts require the **same amount of leather per unit**. The factory has enough leather available each day to produce a maximum of **800 belts** in total (Belt A and Belt B combined).

### Buckle Constraints

| Belt | Buckle Type | Max Available per Day |
|------|-------------|------------------------|
| Belt A | Buckle A | 400 |
| Belt B | Buckle B | 700 |

### Objective

Determine the number of units of Belt A and Belt B to produce each day in order to **maximize total profit**, without exceeding the available production time, leather, or buckle supply.

---

## Linear Programming Formulation

### Decision Variables

- $x$ = number of units of Belt A produced per day
- $y$ = number of units of Belt B produced per day

### Objective Function

Maximize total profit:

$$
Z = 3x + 4y
$$

### Constraints

$$
2x + y \leq 1000 \quad \text{(Production time, in Belt B-equivalent units)}
$$

$$
x + y \leq 800 \quad \text{(Leather availability)}
$$

$$
x \leq 400 \quad \text{(Buckle A availability)}
$$

$$
y \leq 700 \quad \text{(Buckle B availability)}
$$

$$
x \geq 0, \quad y \geq 0 \quad \text{(Non-negativity)}
$$

---

## Notes

- The time constraint is derived from the relationship that Belt A takes twice as long to produce as Belt B, and the factory's maximum daily output of Belt B alone is 1,000 units. Hence, one unit of Belt A consumes the time-equivalent of two units of Belt B, giving $2x + y \leq 1000$.
- This is a four-constraint, two-variable LP problem and can be solved graphically (via feasible region and corner-point analysis) or computationally (e.g., using `PuLP`, `scipy.optimize.linprog`, or Excel Solver).
- Next steps could include: identifying the feasible region, finding corner points, evaluating the objective function at each, and determining the optimal $(x, y)$.
