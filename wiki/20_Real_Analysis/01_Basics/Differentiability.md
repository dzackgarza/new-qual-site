---
order: 35
---

# Differentiability

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
now take the sequence $x_n \da 1/\sqrt{k\pi}$ to get $f'(x_n) = 2\sqrt{k\pi}(-1)^k \convergesto{n\to\infty}\infty$.

:::

