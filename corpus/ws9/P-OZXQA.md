---
schema: qual/card@1
id: P-OZXQA
kind: problem
title: Determine the number of distinct solutions of the equation
classification:
  areas:
  - real-analysis
  topics:
  - rouche
  - holomorphic-functions
relations: []
review: draft
---

::: {.problem title="?"}
Determine the number of distinct solutions of the equation $$e^{z^2} = 5z^5$$ in the unit disk $\{z \in \mathbb{C} : |z| \le 1\}$.
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** Determine the number of distinct solutions of $e^{z^2} = 5z^5$ in the closed unit disk $\{z : |z| \le 1\}$.

<1>1. Setup: write the equation as $5z^5 - e^{z^2} = 0$.
    Proof: $e^{z^2} = 5z^5 \iff 5z^5 - e^{z^2} = 0$.

<1>2. On $|z| = 1$, $|e^{z^2}| < |5z^5|$.
    Proof: $|e^{z^2}| = e^{\Re(z^2)} = e^{\cos 2\theta} \le e < 5 = |5z^5|$ for $z = e^{i\theta}$.

<1>3. $5z^5 - e^{z^2}$ has exactly 5 zeros in $|z| < 1$ counting multiplicity.
    Proof: Rouch\'e's theorem with $f(z) = 5z^5$ and $g(z) = -e^{z^2}$ on $|z| = 1$, using <1>2: $f + g = 5z^5 - e^{z^2}$ has as many zeros as $f$, which has 5 zeros (at 0, with multiplicity 5).

<1>4. None of these zeros is multiple.
    Proof: a multiple zero $z$ satisfies $5z^5 - e^{z^2} = 0$ and $25z^4 - 2ze^{z^2} = 0$; substituting $e^{z^2} = 5z^5$ gives $25z^4 = 10z^6$, so $z = 0$ (excluded, since $e^0 = 1 \ne 0$) or $|z|^2 = 5/2 > 1$; hence no multiple zero lies in $|z| < 1$.

<1>5. The equation has exactly 5 distinct solutions in $|z| \le 1$.
    Proof: <1>3 gives 5 solutions counting multiplicity in $|z| < 1$; <1>4 shows they are distinct; none lies on $|z| = 1$ by the strict inequality <1>2.

<1>6. Q.E.D.
    Proof: <1>1–<1>5 answer the question.
:::
