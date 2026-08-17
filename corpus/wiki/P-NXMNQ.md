---
schema: qual/card@1
id: P-NXMNQ
kind: problem
title: "Suppose that $f:\\mathbb{R}\\to\\mathbb{R}$ satisfies"
classification:
  areas:
  - real-analysis
  topics:
  - differentiation
  - continuity
relations: []
review: draft
solved: true
---

::: problem
Suppose that $f:\mathbb{R}\to\mathbb{R}$ satisfies $f(0)=0$.
Prove that $f$ is differentiable at $x=0$ if and only if there is a function $g:\mathbb{R}\to\mathbb{R}$ which is continuous at $x=0$ and satisfies $f(x)=xg(x)$ for all $x\in\mathbb{R}$.
:::
::: {.solution}
> **AI-Generated Solution**

<1>1. ($\Leftarrow$) If $f(x) = xg(x)$ with $g$ continuous at $0$, then $f$ is differentiable at $0$ with $f'(0) = g(0)$.
Proof: $\frac{f(x) - f(0)}{x - 0} = \frac{xg(x)}{x} = g(x) \to g(0)$ as $x \to 0$ (continuity of $g$ at $0$; also $f(0) = 0\cdot g(0) = 0$).

<1>2. ($\Rightarrow$) If $f$ is differentiable at $0$ (and $f(0) = 0$), define $g(x) = \frac{f(x)}{x}$ for $x \neq 0$ and $g(0) = f'(0)$.
Proof: then $f(x) = xg(x)$ for all $x$ (for $x = 0$ both sides are $0$).

<1>3. $g$ is continuous at $0$: $\lim_{x \to 0} g(x) = \lim_{x \to 0}\frac{f(x)}{x} = \lim_{x \to 0}\frac{f(x) - f(0)}{x - 0} = f'(0) = g(0)$.
Proof: <1>2 and the definition of the derivative (using $f(0) = 0$).

<1>4. Q.E.D. Proof: <1>1 and <1>3 give both directions.
:::
