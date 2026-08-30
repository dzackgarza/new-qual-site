---
order: 101
---

# Gauss-Lucas Theorem

The zeros of a polynomial's derivative lie in the convex hull of the zeros of the polynomial itself.
This is a purely algebraic fact with a short complex-analytic proof.

::: {.theorem}
If $f$ is a nonconstant polynomial and $a_1, \dots, a_n$ are its zeros (counted with multiplicity), then every zero of $f'$ lies in $\operatorname{conv}(\{a_1, \dots, a_n\})$.
:::

**Proof.** Suppose $f'(w) = 0$ with $w \notin \operatorname{conv}(\{a_1, \dots, a_n\})$.
Then there is a hyperplane separating $w$ from the convex hull, so after a rotation we may assume $\operatorname{Re}(a_k) < \operatorname{Re}(w)$ for every $k$.
But then

$$
\frac{f'(w)}{f(w)} = \sum_{k=1}^n \frac{1}{w - a_k}
$$

has $\operatorname{Re}\bigl(\frac{1}{w-a_k}\bigr) > 0$ for each $k$, so $\operatorname{Re}(f'(w)/f(w)) > 0$, contradicting $f'(w) = 0$.
$\qed$

The equality case is sharp: $f(z) = z^n$ has all zeros at the origin, and $f'(z) = nz^{n-1}$ has its zero there too.
More interestingly, the zeros of $f'$ can be strictly interior to the convex hull — take $f(z) = z^3 - 1$, whose zeros are the cube roots of unity and whose derivative $3z^2$ has a double zero at the origin.

A consequence: if all zeros of $f$ lie in a half-plane, then so do all zeros of $f'$, and by induction so do all zeros of every derivative.

[[T-C7GBB]]
