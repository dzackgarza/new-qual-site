---
schema: qual/card@1
id: P-RA-WORKSHOP-D4-W1
kind: problem
title: Uniform continuity and a continuous non-uniformly-continuous example
classification:
  areas:
  - real-analysis
  topics:
  - Uniform Continuity
  - Counterexamples
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
State the definition of uniform continuity.
Give an example of a function $f:(0,1)\to\mathbb R$ which is continuous but not uniformly continuous.
:::

::: {.solution}
<1>1. A function $f:D\to\mathbb R$ is uniformly continuous if for every $\varepsilon>0$ there exists $\delta>0$ such that, for every $x,y\in D$,
\[
|x-y|<\delta\quad\Longrightarrow\quad |f(x)-f(y)|<\varepsilon.
\]

::: {.proof}
This is the definition of uniform continuity. The same $\delta$ depends only on $\varepsilon$, not on the points $x,y$.
:::

<1>2. The function $f:(0,1)\to\mathbb R$ defined by $f(x)=1/x$ is continuous.

::: {.proof}
The reciprocal function is continuous at every nonzero real number, so its restriction to $(0,1)$ is continuous.
:::

<1>3. The function in step <1>2 is not uniformly continuous.

::: {.proof}
Suppose it were uniformly continuous. Apply step <1>1 with $\varepsilon=1$ to obtain $\delta>0$. Choose an integer $n\geq2$ with $1/(2n)<\delta$, and put $x=1/n$ and $y=1/(2n)$. Then $x,y\in(0,1)$ and $|x-y|=1/(2n)<\delta$, while
\[
|f(x)-f(y)|=|n-2n|=n\geq2,
\]
contradicting the required inequality $|f(x)-f(y)|<1$.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>1 states the definition, and steps <1>2–<1>3 establish the requested example.
:::
:::
