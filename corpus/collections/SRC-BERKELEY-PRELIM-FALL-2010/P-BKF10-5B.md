---
schema: qual/card@1
id: P-BKF10-5B
kind: problem
title: $f(x)/x$ is increasing when $f(0)=0$ and $f'$ is increasing
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Problem 5B of the retained Berkeley Fall 2010 preliminary-exam solution packet f10solutions.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the quotient derivative and the mean-value-theorem estimate
    f(x)<=x f'(x); strictness follows as well if "increasing" is read as
    strictly increasing.
---

::: {.problem}
Let $f:[0,\infty)\to\RR$ satisfy:

- $f$ is continuous;

- $f(0)=0$;

- $f$ is differentiable on $(0,\infty)$; and

- $f'$ is increasing on $(0,\infty)$.

Define $g:(0,\infty)\to\RR$ by
$$
g(x)=\frac{f(x)}x.
$$
Show that $g$ is increasing.
:::

::: {.hint}
Differentiate.
:::

::: {.solution}
<1>1. For every $x>0$,
$$
g'(x)=\frac{x f'(x)-f(x)}{x^2}.
$$

::: {.proof}
Since $f$ is differentiable on $(0,\infty)$, the quotient rule gives
$$
g'(x)
=\frac{x f'(x)-f(x)}{x^2}.
$$
:::

<1>2. For every $x>0$,
$$
f(x)\le x f'(x).
$$

::: {.proof}
Fix $x>0$. The function $f$ is continuous on $[0,x]$ and differentiable
on $(0,x)$, so the mean value theorem gives some $c\in(0,x)$ such that
$$
f'(c)
=\frac{f(x)-f(0)}{x-0}
=\frac{f(x)}x.
$$
Because $c<x$ and $f'$ is increasing,
$$
f'(c)\le f'(x).
$$
Multiplying by $x>0$ gives $f(x)\le x f'(x)$. If the hypothesis
"$f'$ is increasing" is understood in the strict sense, then this
inequality is strict.
:::

<1>3. For every $x>0$, one has
$$
g'(x)\ge0.
$$

::: {.proof}
By step <1>2, the numerator $x f'(x)-f(x)$ in the formula from step
<1>1 is nonnegative, while $x^2>0$.
:::

<1>4. The function $g$ is increasing on $(0,\infty)$.

::: {.proof}
Let $0<a<b$. By the mean value theorem applied to $g$ on $[a,b]$,
there exists $c\in(a,b)$ such that
$$
g(b)-g(a)=g'(c)(b-a).
$$
Step <1>3 gives $g'(c)\ge0$, so $g(b)\ge g(a)$. Thus $g$ is increasing
in the nondecreasing sense. Under the strict interpretation of the
hypothesis on $f'$, step <1>2 gives $g'(x)>0$, hence $g$ is strictly
increasing.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 proves the required monotonicity.
:::
:::
