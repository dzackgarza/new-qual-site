---
schema: qual/card@1
id: E-HAT-4.1-2
kind: problem
title: "Functoriality of $\\pi_n$ under homotopy equivalence"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.1, Exercise 2; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: claude
  date: 2026-11-01
  note: >-
    Read line by line. Correct, and the basepoint bookkeeping is stated rather than hidden: a homotopy
    `psi phi ~ id_X` gives a path `eta` from `x_0` to `psi phi (x_0)`, naturality of homotopy groups
    under a homotopy gives `beta_eta (psi phi)_* = id`, and `phi psi ~ id_Y` similarly makes
    `phi_* psi_*` the identity after the corresponding change of basepoint. So `phi_*` is invertible once
    the canonical basepoint isomorphisms are composed in, which is the claim; the `n = 0` remark about
    path components is right as well.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read against Hatcher, Exercise 2 of §4.1, printed p. 358, in
    `tmp/sources/hatcher-2002-algebraic-topology.md` — the exercise carries the bracket "[The case
    $n=1$ is Proposition 1.18.]", which is the page-62 result the card cites — and against DeMason,
    Hatcher 4.1.2, printed p. 89, which the card named without a page. The card's sketch was correct
    but left the naturality step to the reader; the lemma that carries it is proved in the source and
    is now written out on the card: for a homotopy $h_t$ and the track $\gamma(t)=h_{1-t}(x_0)$ one
    has $h_{0*}=\beta_\gamma h_{1*}$, by composing $h_t\circ f$ with the reparametrized path
    $\gamma_t$, the ends being the constant path at $h_0(x_0)$ and $\gamma$. Applied to
    $\psi\varphi$ and to $\varphi\psi$ this gives $\beta_\eta(\psi\varphi)_*=\mathrm{id}$ and
    $\varphi_*\psi_*=\beta_{\eta'}$, whence $\varphi_*$ is injective and surjective. Checked: the
    functoriality $(\varphi\psi)_*=\varphi_*\psi_*$, the direction of $\beta_\eta$ from the group at
    $\psi\varphi(x_0)$ to that at $x_0$, and the $n=0$ remark on path components. No defect.

---

::: {.problem}
Show that if $\varphi: X \to Y$ is a homotopy equivalence, then the induced homomorphisms $\varphi_*: \pi_n(X, x_0) \to \pi_n(Y, \varphi(x_0))$ are isomorphisms for all $n$.
:::

::: {.solution}
Let $\varphi:X\to Y$ be a homotopy equivalence, with homotopy inverse $\psi:Y\to X$. Choose a path $\eta$ from $x_0$ to $\psi\varphi(x_0)$ supplied by the homotopy $\psi\varphi\simeq\operatorname{id}_X$. Naturality of homotopy groups under a homotopy gives
$$
\beta_\eta\circ(\psi\varphi)_*=\operatorname{id}_{\pi_n(X,x_0)},
$$
where $\beta_\eta$ is the appropriate change-of-basepoint isomorphism. Similarly, from $\varphi\psi\simeq\operatorname{id}_Y$ one gets a change-of-basepoint isomorphism making $\varphi_*\psi_*$ the identity.

Thus $\varphi_*$ has a two-sided inverse after the canonical basepoint changes. In particular
$$
\boxed{\varphi_*:\pi_n(X,x_0)\xrightarrow{\cong}\pi_n(Y,\varphi(x_0))}
$$
for every $n\ge1$. (For $n=0$, the same argument says that a homotopy equivalence induces a bijection on path components.)

The case $n=1$ is Hatcher's Proposition 1.18 (p. 62): a homotopy equivalence induces an isomorphism on fundamental groups. For $n\ge2$ the argument above applies verbatim, since the change-of-basepoint isomorphisms $\beta_\eta$ are available in every degree and the homotopies $\psi\varphi\simeq\operatorname{id}_X$, $\varphi\psi\simeq\operatorname{id}_Y$ give the two one-sided inverses up to those basepoint changes. This is the split the DeMason solution set uses (*M382C Full Credit HW Problems*, Hatcher 4.1.2, printed p. 89).

*The naturality step written out* — this is the lemma DeMason proves on the same page. If $h_t:X\to Y$ is a homotopy and $\gamma(t)=h_{1-t}(x_0)$, then $h_{0*}=\beta_\gamma h_{1*}$. For $[f]\in\pi_n(X,x_0)$ the composite $h_t\circ f$ carries $(I^n,\partial I^n)$ to $(Y,h_t(x_0))$; composing it with the reparametrized path $\gamma_t$ that runs along $\gamma$ from $\gamma(1-t)$ to $\gamma(1)=h_0(x_0)$ gives a family of maps $(I^n,\partial I^n)\to(Y,h_0(x_0))$ continuous in $(x,t)$. At $t=0$ the path $\gamma_0$ is constant, so the class is $[h_0\circ f]$; at $t=1$ the path is $\gamma$, so it is $\beta_\gamma[h_1\circ f]$. Hence $\beta_\gamma h_{1*}=h_{0*}$. Applying this to $h_t=\psi\varphi$ gives the displayed $\beta_\eta(\psi\varphi)_*=\mathrm{id}$, and applying it to $h_t=\varphi\psi$ gives $\beta_{\eta'}(\varphi\psi)_*=\mathrm{id}$; then $(\psi\varphi)_*$ is injective with left inverse $\beta_\eta$, so $\varphi_*$ is injective, and $\varphi_*\psi_*=\beta_{\eta'}$ is an isomorphism, so $\varphi_*$ is surjective.
:::
