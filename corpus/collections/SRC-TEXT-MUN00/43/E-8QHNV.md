---
schema: qual/card@1
id: E-8QHNV
kind: problem
title: Uniformly continuous maps extend to the closure
classification:
  areas:
  - topology
  topics:
  - Metric Spaces
  - Continuous Functions
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    Transcribed from the located published solution: "Tze Heng", *Munkres' Topology: Self-study Notes
    and Exercises Attempts*, "Chapter 7", "Exercises Attempts", item under "Exercise after §43" numbered
    2 (URL https://blog.ttheng.com/docs/mathematics/munkres-topology-self-study/chapt-7/exercises/, read
    2026-11-11; a web page has no printed page, so it is cited by URL and date read). Checked against
    Munkres, Topology (2000), §43 Exercise 2, printed p. 270, with the Sequence Lemma (Lemma 21.2), the
    definition of uniform continuity and the fact that a uniformly continuous map takes Cauchy sequences
    to Cauchy sequences. The blog's argument is the one on the card: the extension is defined by
    g(a) = lim f(a_n) along sequences a_n -> a in A, well defined because two such sequences have
    d_X(a_n, b_n) -> 0, completeness of Y supplies the limits, uniform continuity of g follows with the
    factor three bookkeeping on delta/3, and uniqueness because two continuous maps into a Hausdorff
    space that agree on a dense subspace agree. What was corrected: the blog closes the uniform
    continuity with "taking limits over n we have d_Y(g(x), g(y)) < eps", which needs the limit to be
    taken after the delta/3 comparison of d_X(x_n,y_n) is made for all large n; the card writes the
    three-term triangle inequalities explicitly in both X and Y. The card's earlier dangling step
    references, to labels that no step carried, are replaced by the prose sentence that closes the
    solution.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Repaired and restructured. The card was the usual skeleton: a label-step ('Definition and
    well-definedness of the extension g') with a '*Proof:*' marker left inside it and an empty
    pf-proof, followed by seventeen nested one-sentence claims with no justification. It is now
    five proved steps: uniform continuity gives Cauchy-continuity with the modulus written down;
    the limit is independent of the approximating sequence, by the three-epsilon comparison of
    the two images; the extension is defined and extends f; g is uniformly continuous with the
    same modulus (up to thirds); and uniqueness follows from continuity on a dense set. Nothing
    mathematical was changed, and no theorem beyond completeness of Y and the definition of
    uniform continuity is used. Not claimed: a retained solution set; the collection's
    provenance is the Munkres textbook, whose text is not retained here.
---

::: {.exercise}

Let $(X, d_X)$ and $(Y, d_Y)$ be metric spaces; let $Y$ be complete.
Let $A \subset X$.
Show that if $f: A \to Y$ is uniformly continuous, then $f$ can be uniquely extended to a continuous function $g: \overline{A} \to Y$, and $g$ is uniformly continuous.
:::

::: {.solution}
Throughout $(X,d_{X})$ and $(Y,d_{Y})$ are metric spaces with $Y$ complete, $A \subseteq X$, $f\colon A \to Y$ is uniformly continuous, and $\overline{A}$ is the closure of $A$ in $X$. The exercise is Munkres, *Topology* (2000), §43.

::: pf

::: {.pf-step #cauchy}
$f$ carries Cauchy sequences of $A$ to Cauchy sequences of $Y$.

::: pf-proof
Let $\varepsilon > 0$ and let $\delta > 0$ be the modulus of uniform continuity of $f$ for $\varepsilon$: $d_{X}(a,a') < \delta$ implies $d_{Y}\bigl(f(a),f(a')\bigr) < \varepsilon$ for all $a, a' \in A$. If $(a_{n})$ is Cauchy there is $N$ with $d_{X}(a_{n},a_{m}) < \delta$ for $n, m \ge N$, and then $d_{Y}\bigl(f(a_{n}),f(a_{m})\bigr) < \varepsilon$ for those indices; so $\bigl(f(a_{n})\bigr)$ is Cauchy.

:::

:::

::: {.pf-step #well-defined}
For $x \in \overline{A}$ and sequences $(a_{n})$, $(b_{n})$ in $A$ converging to $x$, the sequences $\bigl(f(a_{n})\bigr)$ and $\bigl(f(b_{n})\bigr)$ converge to a common limit in $Y$.

::: pf-proof
Both are Cauchy by step [](#cauchy){.pf-ref}, and $Y$ is complete, so each converges; let $\alpha$, $\beta$ be the limits. Given $\varepsilon > 0$ take $\delta$ from uniform continuity for $\varepsilon/3$; since $a_{n} \to x$ and $b_{n} \to x$ there is $N$ with $d_{X}(a_{n},x) < \delta/2$ and $d_{X}(b_{n},x) < \delta/2$ for $n \ge N$, whence $d_{X}(a_{n},b_{n}) < \delta$ and $d_{Y}\bigl(f(a_{n}),f(b_{n})\bigr) < \varepsilon/3$. For $n$ large the two images are within $\varepsilon/3$ of $\alpha$ and $\beta$, so $d_{Y}(\alpha,\beta) < \varepsilon$; as $\varepsilon$ was arbitrary, $\alpha = \beta$.

:::

:::

::: {.pf-step #define}
$g(x) \coloneqq \lim_{n}f(a_{n})$ for any sequence $a_{n} \to x$ in $A$ defines a function $g\colon\overline{A} \to Y$ extending $f$.

::: pf-proof
Step [](#well-defined){.pf-ref} makes the value independent of the sequence, and for $x \in \overline{A}$ such a sequence exists because $x$ is a limit point of $A$ or a point of $A$ (where the constant sequence serves). For $x \in A$ the constant sequence gives $g(x) = f(x)$, so $g$ extends $f$.

:::

:::

::: {.pf-step #uniform}
$g$ is uniformly continuous on $\overline{A}$.

::: pf-proof
Let $\varepsilon > 0$ and take $\delta$ from the uniform continuity of $f$ for $\varepsilon/3$. Let $x, x' \in \overline{A}$ with $d_{X}(x,x') < \delta/3$. Choose sequences $a_{n} \to x$, $a_{n}' \to x'$ in $A$; for $n$ large, $d_{X}(a_{n},x) < \delta/3$ and $d_{X}(a_{n}',x') < \delta/3$, so $d_{X}(a_{n},a_{n}') < \delta$ and $d_{Y}\bigl(f(a_{n}),f(a_{n}')\bigr) < \varepsilon/3$, while the two images are within $\varepsilon/3$ of $g(x)$ and $g(x')$ for $n$ large. Hence $d_{Y}\bigl(g(x),g(x')\bigr) < \varepsilon$ whenever $d_{X}(x,x') < \delta/3$, which is uniform continuity of $g$.

:::

:::

::: pf-step
The extension is unique: if $h\colon\overline{A} \to Y$ is continuous and agrees with $f$ on $A$, then $h = g$.

::: pf-proof
Let $x \in \overline{A}$ and take $a_{n} \to x$ in $A$. Continuity of $h$ gives $h(x) = \lim_{n}h(a_{n}) = \lim_{n}f(a_{n}) = g(x)$, using $h = f$ on $A$ and the definition of $g$; so $h$ and $g$ agree at every point of $\overline{A}$. Together with steps [](#define){.pf-ref} and [](#uniform){.pf-ref} this is the assertion.

:::

:::

:::
:::
