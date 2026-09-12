---
schema: qual/card@1
id: P-RASP08F
kind: problem
title: "Translation of distributions and distributional derivative"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 6 of the official UCSD Spring 2008 real-analysis qualifying exam; Fourier phase uses the repository convention exp(-2 pi i x xi).
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
For $f : \mathbb{R} \to \mathbb{C}$ and $h \in \mathbb{R}$, denote by $\tau_h f : \mathbb{R} \to \mathbb{C}$ the function defined by $\tau_h f(x) := f(x + h)$ for all $x \in \mathbb{R}$.

(a) Show that if $T$ is a distribution on $\mathbb{R}$ and $h \in \mathbb{R}$, then
$$
\tau_h T(\phi) := T(\tau_{-h}\phi), \qquad \phi \in C_0^\infty(\mathbb{R}),
$$
defines a distribution $\tau_h T$ on $\mathbb{R}$.

(b) Show that the following holds in $\mathcal{D}'(\mathbb{R})$:
$$
\lim_{h \to 0} \frac{\tau_h T - T}{h} = T'.
$$

(c) Show that if $T$ is a tempered distribution then $\tau_h T$ is also a tempered distribution.
Find the Fourier transform of $\tau_h T$ in terms of the Fourier transform of $T$.
:::


::: solution
<1>1. Translation preserves distributions.
::: proof
Fix $h\in\mathbb R$. The map
\[
\phi\longmapsto \tau_{-h}\phi,
\qquad
(\tau_{-h}\phi)(x)=\phi(x-h),
\]
is a continuous linear automorphism of $C_c^\infty(\mathbb R)$: derivatives commute with translation, and the support is merely translated by $h$.

Therefore the composition
\[
\tau_hT(\phi):=T(\tau_{-h}\phi)
\]
is linear and continuous on $C_c^\infty(\mathbb R)$. Hence $\tau_hT\in\mathcal D'(\mathbb R)$.
:::

<1>2. Recover the distributional derivative from difference quotients.
::: proof
For every test function $\phi$,
\[
\left(\frac{\tau_hT-T}{h}\right)(\phi)
=T\left(\frac{\tau_{-h}\phi-\phi}{h}\right).
\]
In $C_c^\infty(\mathbb R)$,
\[
\frac{\tau_{-h}\phi-\phi}{h}
=\frac{\phi(\cdot-h)-\phi}{h}
\longrightarrow -\phi'
\qquad(h\to0).
\]
Indeed, the convergence holds uniformly for every derivative on one fixed compact set containing the supports for all sufficiently small $h$.

By continuity of $T$,
\[
\left(\frac{\tau_hT-T}{h}\right)(\phi)
\longrightarrow T(-\phi')
=T'(\phi).
\]
Thus
\[
\boxed{
\frac{\tau_hT-T}{h}\longrightarrow T'
\quad\text{in }\mathcal D'(\mathbb R).}
\]
:::

<1>3. Translation preserves tempered distributions.
::: proof
If $T\in\mathcal S'(\mathbb R)$, then translation is a continuous linear automorphism of the Schwartz space. Indeed, for every pair of nonnegative integers $m,k$,
\[
\sup_x |x^m(\tau_{-h}\phi)^{(k)}(x)|
=\sup_x |x^m\phi^{(k)}(x-h)|
\]
is bounded by a finite linear combination of Schwartz seminorms of $\phi$, because $x=(x-h)+h$. Hence
\[
\phi\mapsto T(\tau_{-h}\phi)
\]
is continuous on $\mathcal S$, so $\tau_hT\in\mathcal S'$.
:::

<1>4. Compute the Fourier transform.
::: proof
With the convention
\[
\widehat\phi(\xi)=\int_{\mathbb R}\phi(x)e^{-2\pi i x\xi}\,dx,
\]
one has for ordinary Schwartz functions
\[
\widehat{\tau_h\phi}(\xi)
=e^{2\pi i h\xi}\widehat\phi(\xi),
\]
because $\tau_h\phi(x)=\phi(x+h)$.

The same identity extends by duality to tempered distributions. Therefore
\[
\boxed{
\widehat{\tau_hT}
=e^{2\pi i h\xi}\widehat T.}
\]
:::
:::
