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
- event: source-corrected
  by: claude
  date: 2026-11-20
  note: >-
    Citation convention. Sources on this card are cited by chapter, section and numbered statement
    only, and the statement and solution above cite every source by its numbered statement. The
    events dated before today are left as their sessions wrote them, which QUAL-11 requires, so a
    locator in one of them stands as a historical record and is superseded by the citation now on
    the card. This event records the convention and claims no further reading: the
    mathematics of the card is as those events describe it.
- event: source-corrected
  by: claude
  date: 2026-11-20
  note: >-
    Citation corrected. Example 4.11, "Cellular Approximation for Pairs", is now cited by name,
    and Theorem 4.8 with it. The event of 2026-11-19 is left as written under QUAL-11.
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Read against Hatcher, Algebraic Topology (2002), §4.3 Exercise 5, printed p. 419,
    Theorem 4.57, printed p. 393, and Example 4.11, printed p. 349. The proof is correct:
    K(Z,n) is built from S^n with cells of dimension at least n+2, so its (n+1)-skeleton
    is S^n; surjectivity of [X,S^n] -> [X,K(Z,n)] is cellular approximation for the
    n-dimensional X, and injectivity is cellular approximation for the pair
    (X x I, X x dI), whose total space is (n+1)-dimensional, landing in
    K(Z,n)^{n+1} = S^n. What the card did not say is the identification it was using:
    Theorem 4.57 is stated for based classes, the exercise writes unbased [X,S^n], and
    those agree here because pi_1(S^n) acts trivially (0 for n >= 2, and conjugation in
    the abelian pi_1(S^1) = Z for n = 1). A sentence now says so. Statement unchanged.
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
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Structured into Lamport steps from the card's own prose. The construction of K(Z,n) from S^n
    by attaching cells of dimension at least n+2 is now a step, with the reason the (n+1)-skeleton
    stays S^n and pi_n stays Z (cells of dimension above n+1 do not change pi_n, by cellular
    approximation of spheres and homotopies of dimension at most n). Surjectivity uses cellular
    approximation of maps out of the n-dimensional X; injectivity uses cellular approximation for
    the pair (X x I, X x dI), which is legitimate because X x I is (n+1)-dimensional and the
    homotopy is already cellular on the subcomplex; representability of H^n(-;Z) by K(Z,n) is
    cited from section 4.3. Statement and printed hint unchanged; the card says the argument is
    its own.
- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    Notation repair after the corpus check reported raw TeX the page cannot show. One sentence
    cites the representability theorem by section as `\S4.3`, a section sign written as a TeX
    command outside a math span, which the HTML writer drops; it now reads the character `§4.3`,
    as the corpus does elsewhere. Mathematics and wording unchanged.
- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    The card said no retained solution set covers this exercise, and that is false: Sam's set,
    retained as `tmp/sources/hatcher-solutions-sam-2008.pdf`, solves it at §4.3 Exercise 5 on
    printed p. 25. The rendered sentence now cites it and says what the card adds. Found by
    screening the residue's absence claims against the solution sets inventoried in
    `wiki/topology/resources/solutions.md`; no step of the proof changed.
- event: solution-reviewed
  by: claude
  date: 2026-11-22
  note: >-
    Read against Hatcher, §4.3 Exercise 5, and against Sam's §4.3 Exercise 5, which is retained and
    whose argument the card transcribes: build $K(\ZZ,n)$ from $S^n$ by attaching cells of dimension
    $\ge n+2$ so that the $(n+1)$-skeleton stays $S^n$; cellular approximation puts every map of the
    $n$-dimensional $X$, and every homotopy of such maps, into that skeleton, giving surjectivity and
    injectivity of $[X,S^n]\to[X,K(\ZZ,n)]$; Theorem 4.57 identifies the latter with $H^n(X;\ZZ)$.
    One correction: the construction step said the groups $\pi_i$ for $i\le m$ are unchanged by
    attaching $(m+1)$-cells, but $\pi_m$ is exactly what those cells kill; it now says $\pi_i$ for
    $i<m$ is unchanged and $\pi_m$ loses the classes killed. The remaining steps are unchanged and
    correct, including the paragraph identifying unbased with based classes.
- event: solution-reviewed
  by: claude
  date: 2026-11-22
  note: >-
    Repair of the construction, from an independent review. It began the killing induction at
    $m=n+2$, which omits $\pi_{n+1}$: that group need not vanish — $\pi_3(S^2)\cong\ZZ$ — and it is
    killed by attaching $(n+2)$-cells, so the induction must start at $m=n+1$. The step now starts
    there, records the counterexample, and keeps the conclusion: no cells of dimension $\le n+1$ are
    ever attached, so the $(n+1)$-skeleton stays $S^n$ and the result is a $K(\ZZ,n)$.
---

::: {.problem}
Show that $[X, S^n] \approx H^n(X; \ZZ)$ if $X$ is an $n$-dimensional CW complex. [Build a $K(\ZZ, n)$ from $S^n$ by attaching cells of dimension $\geq n + 2$.]
:::

::: {.solution}
Take $j\colon S^n\to K(\ZZ,n)$ the inclusion of the $n$-skeleton in a $K(\ZZ,n)$ built as the hint prescribes, so that $K(\ZZ,n)^k=S^n$ for $n\le k\le n+1$. Cellular approximation makes every map out of the $n$-dimensional $X$ land in $S^n$, which gives surjectivity, and makes every homotopy out of $X\times I$ land in $K(\ZZ,n)^{n+1}=S^n$, which gives injectivity; representability of $H^n(-;\ZZ)$ finishes. The argument is that of the retained solution set: **Steven V. Sam, *Solutions to Algebraic Topology* (2008), §4.3 Exercise 5** of `tmp/sources/hatcher-solutions-sam-2008.pdf`, which builds $K(\ZZ,n)$ from $S^n$ by attaching cells of dimension $\ge n+2$, obtains injectivity and surjectivity from cellular approximation, and concludes through $[X,K(\ZZ,n)]\cong H^n(X;\ZZ)$. The card states the identification of the unbased and based class sets that the argument uses.

::: pf

::: {.pf-step #build}
There is a CW complex $K(\ZZ,n)$ with a map $j\colon S^n\to K(\ZZ,n)$, an isomorphism on $\pi_n$, such that $K(\ZZ,n)^k=S^n$ for $n\le k\le n+1$.

::: pf-proof
Begin with $S^n$. Inductively, for $m\ge n+1$, if $\pi_{m}(-)\ne0$, choose maps $S^m\to K$ generating it and attach $(m+1)$-cells along them; each attachment kills the corresponding class, and because the attached cells have dimension $m+1>m$, the groups $\pi_i$ for $i<m$ are unchanged and $\pi_m$ loses exactly the classes killed (cellular approximation of maps of $S^i$ and of homotopies of them, for $i<m<m+1$). The induction must start at $m=n+1$, not at $n+2$: $\pi_{n+1}(S^n)$ need not vanish — for $n=2$ it is $\pi_3(S^2)\cong\ZZ$ — and it is killed by attaching $(n+2)$-cells, which is the first step. Since every cell attached from then on has dimension at least $n+2$, no cells of dimension $n+1$ or below are ever attached, so the $(n+1)$-skeleton of the result is $S^n$ itself, and the result has $\pi_n=\ZZ$ and no other homotopy. So it is a $K(\ZZ,n)$ and $j$ is the inclusion of its $n$-skeleton.
:::

:::


::: {.pf-step #surj}
$j_*\colon[X,S^n]\to[X,K(\ZZ,n)]$ is surjective.

::: pf-proof
Let $f\colon X\to K(\ZZ,n)$ be any map, with $X$ $n$-dimensional. By cellular approximation (Theorem 4.8) $f$ is homotopic to a cellular map $f'$, and a cellular map out of an $n$-dimensional complex lands in the $n$-skeleton of the target, which is $S^n$ by step [](#build){.pf-ref}. So $f'$ is a map $X\to S^n$ with $j\,f'\simeq f$, i.e. $j_*[f']=[f]$.
:::

:::


::: {.pf-step #inj}
$j_*$ is injective.

::: pf-proof
Let $c_0,c_1\colon X\to S^n$ be cellular with $j\,c_0\simeq j\,c_1$, and let $G\colon X\times I\to K(\ZZ,n)$ be a homotopy. On the subcomplex $X\times\partial I$ the map $G$ is $j\,c_0$ and $j\,c_1$, hence cellular. Since $X\times I$ is $(n+1)$-dimensional, cellular approximation for the pair (Example 4.11) gives a cellular $G'$ homotopic to $G$ relative to $X\times\partial I$, and a cellular map out of an $(n+1)$-dimensional complex lands in $K(\ZZ,n)^{n+1}=S^n$ by step [](#build){.pf-ref}. So $G'$ is a homotopy in $S^n$ from $c_0$ to $c_1$, and the two classes agree.
:::

:::


::: {.pf-step #bij}
$j_*\colon[X,S^n]\to[X,K(\ZZ,n)]$ is a bijection of pointed sets.

::: pf-proof
Surjective by step [](#surj){.pf-ref} and injective by step [](#inj){.pf-ref}; a map of pointed sets that is both is a bijection, and it carries the basepoint to the basepoint because $j$ does.
:::

:::


::: {.pf-step #represent}
$[X,K(\ZZ,n)]\cong H^n(X;\ZZ)$ for a CW complex $X$ and $n\ge1$.

::: pf-proof
Eilenberg--MacLane spaces represent cohomology: $[f]\mapsto f^*\iota$ is a natural bijection $[X,K(\ZZ,n)]\to H^n(X;\ZZ)$, where $\iota\in H^n(K(\ZZ,n);\ZZ)$ is the fundamental class; this is the representability theorem of §4.3.
:::

:::


::: {.pf-step #conclusion}
$[X,S^n]\cong H^n(X;\ZZ)$ for every $n$-dimensional CW complex $X$ and every $n\ge1$.

::: pf-proof
Composing the bijection of step [](#bij){.pf-ref} with step [](#represent){.pf-ref} gives $[X,S^n]\cong[X,K(\ZZ,n)]\cong H^n(X;\ZZ)$, which is the assertion of the exercise. Two brackets are in play and coincide here: Theorem 4.57 is stated for based homotopy classes $\langle X,K(\ZZ,n)\rangle$, while the exercise writes $[X,S^n]$ for unbased ones. For a CW complex $X$ and a path-connected $Y$ the unbased classes are the orbits of $\langle X,Y\rangle$ under the action of $\pi_1(Y)$, and here that action is trivial: $\pi_1(S^n)=0$ for $n\ge2$, and for $n=1$ the action is conjugation in the abelian group $\pi_1(S^1)=\ZZ$. So $[X,S^n]=\langle X,S^n\rangle$, and the bijections above identify all three. The hypothesis $n\ge1$ is the one under which the hint's construction starts from $S^n$ and under which representability is stated; the exercise is posed for $n$-dimensional complexes with $n\ge1$.
:::

:::

:::
:::
