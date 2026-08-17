---
schema: qual/card@1
id: P-MMAQ-Q5ZWN3J46V
kind: problem
title: "Let $f, g: [a, b] \\to \\RR$ be measurable with $\\int_{a}^{b} f(x) ~d x=\\int_{a}^{b} g(x) ~d x$"
classification:
  areas:
  - real-analysis
  topics:
  - measure-theory
relations: []
review: draft
---

::: problem
Let $f, g: [a, b] \to \RR$ be measurable with
$$
\int_{a}^{b} f(x) ~d x=\int_{a}^{b} g(x) ~d x.
$$

Show that either

1. $f(x) = g(x)$ almost everywhere, or

2. There exists a measurable set $E \subset [a, b]$ such that
   $$
   \int_{E} f(x) ~d x>\int_{E} g(x) ~d x
   $$
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** If $f, g$ are measurable on $[a,b]$ with $\int_a^b f = \int_a^b g$ (finite, so $f, g \in L^1$), then either $f = g$ a.e., or there is a measurable $E \subseteq [a,b]$ with $\int_E f > \int_E g$.

<1>1. Either $m(\{x : f(x) > g(x)\}) = 0$ or $m(\{x : f(x) > g(x)\}) > 0$; these are the only two possibilities.
    Proof: Law of trichotomy for the measure of a set.

<1>2. Case 1: $m(\{f > g\}) = 0$. Then $f \leq g$ a.e., and since $\int (g - f) = 0$ with $g - f \geq 0$ a.e., we get $g - f = 0$ a.e., i.e. $f = g$ a.e.
    <2>1. $f \leq g$ almost everywhere.
        Proof: $\{f > g\}$ has measure zero by the case hypothesis.
    <2>2. $\int_a^b (g - f) ~dx = 0$.
        Proof: Linearity of the integral and the hypothesis $\int f = \int g$.
    <2>3. A nonnegative measurable function with integral $0$ is $0$ almost everywhere.
        Proof: Standard lemma: if $h \geq 0$ and $\int h = 0$, then $h = 0$ a.e. (otherwise $\{h > 0\} = \bigcup_n \{h \geq 1/n\}$ would contain a set of positive measure, on which $\int h > 0$).
    <2>4. Hence $g - f = 0$ a.e., so $f = g$ a.e.
        Proof: By <2>1, $g - f \geq 0$ a.e.; apply <2>3 to $h = g - f$ with <2>2.
    <2>5. Q.E.D.
        Proof: This gives alternative (1).

<1>3. Case 2: $m(\{f > g\}) > 0$. Set $E \definedas \{x : f(x) > g(x)\}$; then $E$ is measurable and $\int_E f > \int_E g$.
    <2>1. $E = \{f > g\}$ is measurable.
        Proof: $f - g$ is measurable, so $\{f - g > 0\}$ is measurable.
    <2>2. $\int_E (f - g) ~dx > 0$.
        Proof: $f - g > 0$ on $E$ by definition, and $m(E) > 0$ by the case hypothesis; the integral of a strictly positive measurable function over a positive-measure set is strictly positive (write $E = \bigcup_n E_n$ with $E_n = \{f - g \geq 1/n\}$; since $m(E) > 0$, some $E_n$ has positive measure, and $\int_E (f-g) \geq \frac{1}{n} m(E_n) > 0$).
    <2>3. Hence $\int_E f - \int_E g = \int_E (f - g) > 0$, i.e. $\int_E f > \int_E g$.
        Proof: Linearity of the integral restricted to $E$ (or $\int_E f = \int f \chi_E$, linear in $f$).
    <2>4. Q.E.D.
        Proof: This gives alternative (2).

<1>4. Conclusion.
    Proof: The two cases of <1>1 exhaust all possibilities; <1>2 handles the first and <1>3 the second, so either (1) or (2) holds.
:::
