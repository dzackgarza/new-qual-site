---
title: Convolution
order: 0
problems:
  topics:
  - Convolution
  - Approximations to the Identity
---

# Convolution

::: {.remark title="Every property is Tonelli"}
$f * g(x) \da \int f(x-y)g(y)\dy$ is defined by an integral in one variable depending on a parameter, so every statement about it is a statement about a double integral:

- well-definedness a.e. and $\norm{f*g}_1 \leq \norm f_1\norm g_1$: Tonelli on $\abs{f(x-y)g(y)}$;

- commutativity and associativity: the change of variables $y \mapsto x-y$, then Fubini;

- Young's inequality $\norm{f*g}_r \leq \norm f_p\norm g_q$ with $\frac1r = \frac1p + \frac1q - 1$: Hölder inside Tonelli.

So a convolution problem is a [[real-analysis/fubini-tonelli/index|Fubini--Tonelli]] problem, and the only question is whether the absolute value has finite iterated integral.
:::

::: {.remark title="Smoothing"}
Convolution inherits the better regularity of its two factors: $f * g$ is as smooth as the smoother of them, and $\partial(f*g) = (\partial f) * g$ whenever the right side makes sense.
That is the mechanism behind approximate identities and behind every density argument in $L^p$: convolving with a smooth bump produces a smooth approximation, and letting the bump concentrate recovers the original.
:::

## Approximate identities

[[T-HHFGB]]

[[T-3UXK7]]

[[PR-PRSKG]]

[[PR-A7UFG]]
