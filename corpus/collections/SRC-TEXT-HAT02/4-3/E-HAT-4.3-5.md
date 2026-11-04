---
schema: qual/card@1
id: E-HAT-4.3-5
kind: problem
title: "$[X, S^n] \\approx H^n(X; \\ZZ)$ for $n$-dimensional $X$"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.3, Exercise 5; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-corrected
  by: claude
  date: 2026-11-01
  note: >-
    Statement repaired against Hatcher's printed text: the card had dropped printed matter
    (a bracketed hint or pointer, or a printed sentence) that an audit located by word-by-word
    comparison with tmp/hat/AT.txt, and that this session re-verified at the cited lines before
    applying the repair. The restored text is the printed wording and the mathematics of the
    statement is otherwise unchanged.
- event: solution-reviewed
  by: claude
  date: 2026-11-01
  note: >-
    Proof read against Hatcher Sec. 4.3 Exercise 5 with its hint (AT.txt 20768-20769) and repaired. The
    card asserted the bijection [X,S^n] = [X,K(Z,n)] by appeal to "obstruction theory or cellular
    induction", which is the substance of the exercise and was neither proved nor cited; the card now
    derives it from the hint's model of K(Z,n) built from S^n with cells of dimension >= n+2, whose
    skeleta in degrees n and n+1 are those of S^n. Surjectivity: a cellular map out of the
    n-dimensional X lands in the n-skeleton. Injectivity: a homotopy X x I -> K(Z,n) is cellular on
    X x dI and X x I has dimension n+1, so relative cellular approximation (Example 4.11) makes it
    land in S^n. Verified as correct and left unchanged: pi_i(S^n) = pi_i(K(Z,n)) for i <= n, and the
    final appeal to representability. Not checked: nothing outside this exercise.

---

::: {.problem}
Show that $[X, S^n] \approx H^n(X; \ZZ)$ if $X$ is an $n$-dimensional CW complex. [Build a $K(\ZZ, n)$ from $S^n$ by attaching cells of dimension $\geq n + 2$.]
:::

::: {.solution}
Choose a map
$$
j:S^n\to K(\ZZ,n)
$$
representing the generator of $\pi_nK(\ZZ,n)$. It induces an isomorphism on $\pi_i$ for $i\le n$: both spaces have zero homotopy groups below $n$, and $j_*:\pi_n(S^n)\to\ZZ$ is an isomorphism.

Take $K(\ZZ,n)$ as the hint prescribes, built from $S^n$ by attaching only cells of dimension $\ge n+2$; then $K(\ZZ,n)^k=S^n$ for $n\le k\le n+1$. Give $X$ its CW structure. By cellular approximation (Theorem 4.8) every map $X\to K(\ZZ,n)$ is homotopic to a cellular one, and a cellular map from the $n$-dimensional $X$ lands in $K(\ZZ,n)^n=S^n$; so $j_*$ is surjective. For injectivity, let $c_0,c_1:X\to S^n$ be cellular maps that become homotopic in $K(\ZZ,n)$, and let $G:X\times I\to K(\ZZ,n)$ be a homotopy between them. It is cellular on the subcomplex $X\times\partial I$, and $X\times I$ has dimension $n+1$, so by cellular approximation for pairs (Example 4.11) $G$ is homotopic relative to $X\times\partial I$ to a cellular map, which lands in $K(\ZZ,n)^{n+1}=S^n$. Hence $c_0\simeq c_1$ in $S^n$ and $j_*$ is injective. Therefore
$$
j_*:[X,S^n]\xrightarrow{\cong}[X,K(\ZZ,n)].
$$

Finally representability gives
$$
[X,K(\ZZ,n)]\cong H^n(X;\ZZ).
$$
Therefore
$$
\boxed{[X,S^n]\cong H^n(X;\ZZ).}
$$
:::
