---
schema: qual/card@1
id: E-MUN-2-4
kind: problem
title: Composition of functions and injectivity and surjectivity
classification:
  areas:
  - topology
  topics:
  - Functions
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 2, Exercise 4; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

Let $f: A \to B$ and $g: B \to C$ .

(a) If $C_0 \subset C$, show that $(g \circ f)^{-1}(C_0) = f^{-1}(g^{-1}(C_0))$ .

(b) If $f$ and $g$ are injective, show that $g \circ f$ is injective.

(c) If $g \circ f$ is injective, what can you say about injectivity of $f$ and $g$ ?

(d) If $f$ and $g$ are surjective, show that $g \circ f$ is surjective.

(e) If $g \circ f$ is surjective, what can you say about surjectivity of $f$ and $g$ ?

(f) Summarize your answers to (b)-(e) in the form of a theorem.
:::

::: {.solution}
(a) For \(a\in A\),
\[
a\in(g\circ f)^{-1}(C_0)
\iff g(f(a))\in C_0
\iff f(a)\in g^{-1}(C_0)
\iff a\in f^{-1}(g^{-1}(C_0)).
\]

(b) If \(g(f(a_1))=g(f(a_2))\), injectivity of \(g\) gives \(f(a_1)=f(a_2)\), and injectivity of \(f\) then gives \(a_1=a_2\). Thus \(g\circ f\) is injective.

(c) If \(g\circ f\) is injective, then \(f\) must be injective: \(f(a_1)=f(a_2)\) implies \(g(f(a_1))=g(f(a_2))\). Nothing follows about injectivity of \(g\) away from \(f(A)\). For example, the inclusion \(f:\{0\}\to\{0,1\}\) followed by the constant map \(g:\{0,1\}\to\{*\}\) has injective composite from a singleton, while \(g\) is not injective.

(d) Given \(c\in C\), choose \(b\in B\) with \(g(b)=c\), then \(a\in A\) with \(f(a)=b\). Thus \((g\circ f)(a)=c\), so the composite is surjective.

(e) If \(g\circ f\) is surjective, then \(g\) is surjective: every \(c\in C\) equals \(g(f(a))\) for some \(a\). Nothing follows about surjectivity of \(f\). For example, the inclusion \(f:\{0\}\to\{0,1\}\) followed by the constant map \(g:\{0,1\}\to\{*\}\) has surjective composite although \(f\) is not surjective.

(f) Therefore:
- the composite of injective maps is injective, and injectivity of a composite forces the first map to be injective;
- the composite of surjective maps is surjective, and surjectivity of a composite forces the second map to be surjective.
:::
