---
schema: qual/card@1
id: E-YR05O
kind: problem
title: Antipode-preserving maps of the circle act by odd powers
classification:
  areas:
  - topology
  topics:
  - Borsuk-Ulam Theorem
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.exercise}

Let $h: S^1 \to S^1$ be continuous and antipode-preserving with $h(b_0) = b_0$.
Show that $h_*$ carries a generator of $\pi_1(S^1, b_0)$ to an odd power of itself.
[Hint: If $k$ is the map constructed in the proof of Theorem 57.1, show that $k_*$ does the same.]
:::

::: {.solution}
Identify \(S^1\) with \(\mathbb R/\mathbb Z\) by \(t\mapsto e^{2\pi it}\), and take \(b_0=1\). Since \(h(b_0)=b_0\), lift \(h\) to a continuous map
\[
H:\mathbb R\to\mathbb R
\]
with \(H(0)=0\) and
\[
e^{2\pi iH(t)}=h(e^{2\pi it}).
\]

Antipode preservation gives
\[
h(e^{2\pi i(t+1/2)})=-h(e^{2\pi it}),
\]
so
\[
H(t+1/2)-H(t)\in \frac12+\mathbb Z.
\]
The left side is continuous in \(t\), while \(\frac12+\mathbb Z\) is discrete; hence it is constant. Thus for some \(m\in\mathbb Z\),
\[
H(t+1/2)=H(t)+m+\frac12
\]
for all \(t\). Applying this twice,
\[
H(t+1)=H(t)+2m+1.
\]
Therefore the degree of \(h\) is the odd integer \(2m+1\). If \(a\) denotes the standard generator of \(\pi_1(S^1,b_0)\cong\mathbb Z\), then
\[
h_*(a)=a^{\,2m+1},
\]
an odd power of the generator, as required.
:::
