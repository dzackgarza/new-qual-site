---
order: 35
problems:
  topics:
  - Differentiation
  - Mean Value Theorem
---

# Differentiability

The mean value theorem is the bridge from pointwise derivative information to global
estimates.  A bounded derivative gives a Lipschitz bound, while differentiating a limit
or series term-by-term requires uniform control strong enough to pass the derivative
through the limit.  None of these statements says that the derivative of a bounded
function must itself be bounded; the example below is the standard counterexample.

[[T-OXNTU]]

[[T-DS4VW]]

[[PR-LTRLV]]

[[FR-EDJWQ]]

[[T-TR526]]

:::{.example title="Derivatives of bounded functions need not be bounded"}
\[
f(x) \da 
\begin{cases}
x^2 \sin\qty{1\over x^2} &  x\neq 0
\\
0 & x=0.
\end{cases}
.\]

Note that $f$ is differentiable at $x=0$ since ${1\over h}\abs{f(h) - f(0)} = \abs{ h\sin\qty{h^{-2}}}\leq \abs{h}\to 0$, and
\[
f'(x) = 2x\sin\qty{1\over x^2 } - \qty{2\over x}\cos\qty{1\over x^2} \chi_{x\neq 0}
.\]
Now take $x_k \da 1/\sqrt{k\pi}$.  Then
\[
f'(x_k)=-2\sqrt{k\pi}(-1)^k,
\qquad
\abs{f'(x_k)}=2\sqrt{k\pi}\longrightarrow\infty,
\]
so $f'$ is unbounded.

:::
