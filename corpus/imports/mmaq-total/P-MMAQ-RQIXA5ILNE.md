---
schema: qual/card@1
id: P-MMAQ-RQIXA5ILNE
kind: problem
title: "Let $f(x) = x^2$ and $E \\subset [0, \\infty) \\definedas \\RR^+$. Show that $m^(E) = 0 \\iff m^(f(E)) = 0$ Deduce that the map \\begin{align} \\phi: \\mathcal{L}(\\RR^+) &\\to \\mathcal{L}(\\RR^+) \\\\ E &\\mapsto f(E) \\end{align}\u2026"
classification:
  areas:
  - real-analysis
  topics:
  - measure-theory
relations: []
review: draft
---

::: problem
Let $f(x) = x^2$ and $E \subset [0, \infty) \definedas \RR^+$.

1. Show that
   $$
   m^*(E) = 0 \iff m^*(f(E)) = 0.
   $$

2. Deduce that the map

`\begin{align*} \phi: \mathcal{L}(\RR^+) &\to \mathcal{L}(\RR^+) \\ E &\mapsto f(E) \end{align*}`{=tex} is a bijection from the class of Lebesgue measurable sets of $[0, \infty)$ to itself.
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** For $f(x) = x^2$ on $\RR^+ = [0, \infty)$: (1) prove $m^*(E) = 0 \iff m^*(f(E)) = 0$ for $E \subseteq \RR^+$; (2) deduce that $E \mapsto f(E)$ is a bijection of the Lebesgue-measurable subsets of $\RR^+$ onto themselves.

<1>1. $x \mapsto x^2$ sends null sets to null sets.
    <2>1. On each bounded interval $[0, N]$, $f$ is Lipschitz with constant $2N$: $\abs{x^2 - y^2} = \abs{x - y}(x + y) \leq 2N \abs{x - y}$.
        Proof: Factor the difference of squares; $x + y \leq 2N$ on $[0, N]$.
    <2>2. A Lipschitz map sends null sets to null sets.
        Proof: If $m^*(A) = 0$ and $A \subseteq [0, N]$, cover $A$ by intervals $(a_j, b_j)$ with $\sum_j (b_j - a_j) < \eps/(2N)$; the images have total length $\leq \sum_j 2N(b_j - a_j) < \eps$ (Lipschitz bound applied to each image interval, whose length is $\leq 2N(b_j - a_j)$), so $m^*(f(A)) \leq \eps$.
    <2>3. If $m^*(E) = 0$, then $m^*(f(E)) = 0$.
        Proof: $E = \bigcup_{k=1}^\infty (E \cap [0, k])$, each $E \cap [0,k]$ is null, so each image is null by <2>1, <2>2; $f(E) = \bigcup_k f(E \cap [0,k])$ is a countable union of null sets, hence null.
    <2>4. Q.E.D.
        Proof: This proves the forward direction of (1).

<1>2. $y \mapsto \sqrt{y}$ sends null sets to null sets.
    <2>1. On $[\delta, \infty)$, $\sqrt{\cdot}$ is Lipschitz: $\abs{\sqrt{u} - \sqrt{v}} = \frac{\abs{u - v}}{\sqrt{u} + \sqrt{v}} \leq \frac{\abs{u - v}}{2\sqrt{\delta}}$.
        Proof: Rationalize the numerator; $\sqrt{u} + \sqrt{v} \geq 2\sqrt{\delta}$ on $[\delta, \infty)$.
    <2>2. Near $0$: $\abs{\sqrt{u} - \sqrt{v}} \leq \sqrt{\abs{u - v}}$ for all $u, v \geq 0$.
        Proof: If $u \geq v$, then $\abs{\sqrt{u} - \sqrt{v}} = \sqrt{u} - \sqrt{v}$ and $(\sqrt{u} - \sqrt{v})^2 = u + v - 2\sqrt{uv} \leq u - v$, so $\sqrt{u} - \sqrt{v} \leq \sqrt{u - v}$.
    <2>3. The map $\sqrt{\cdot}$ sends null sets to null sets.
        Proof: Let $A$ be a null set. Split $A \cap [0, 1]$ into the dyadic annuli $A_k \definedas A \cap [2^{-k}, 2^{-k+1}]$, $k \geq 1$, together with $A \cap \{0\}$. On each annulus, $\sqrt{\cdot}$ is Lipschitz: for $x, y \in [2^{-k}, 2^{-k+1}]$, $\abs{\sqrt x - \sqrt y} = \frac{\abs{x - y}}{\sqrt x + \sqrt y} \leq 2^{k/2 - 1} \abs{x - y}$, since $\sqrt x, \sqrt y \geq 2^{-k/2}$. Each $A_k$ is a subset of the null set $A$, hence null, and its image under a Lipschitz map is null (<1>1<2>2); $\{0\}$ maps to $\{0\}$, null. So $\sqrt{A \cap [0,1]}$ is a countable union of null sets, hence null. For $A \cap [1, \infty)$, $\sqrt{\cdot}$ is Lipschitz (<2>1 with $\delta = 1$), so the image is null as well. Hence $\sqrt A$ is null.
    <2>4. Q.E.D.
        Proof: By <2>1–<2>3, $\sqrt{\cdot}$ preserves null sets.

<1>3. If $m^*(f(E)) = 0$, then $m^*(E) = 0$; hence $m^*(E) = 0 \iff m^*(f(E)) = 0$.
    <2>1. $E \subseteq f^{-1}(f(E)) = \sqrt{f(E)}$, where $\sqrt{A} \definedas \theset{y \geq 0 : y^2 \in A}$.
        Proof: For $e \in E$, $f(e) = e^2 \in f(E)$, so $e = \sqrt{e^2} \in \sqrt{f(E)}$.
    <2>2. $m^*(\sqrt{f(E)}) = 0$ when $m^*(f(E)) = 0$.
        Proof: By <1>2, $\sqrt{\cdot}$ sends the null set $f(E)$ to a null set.
    <2>3. Hence $m^*(E) \leq m^*(\sqrt{f(E)}) = 0$, so $m^*(E) = 0$.
        Proof: Monotonicity of outer measure (<2>1), then <2>2.
    <2>4. Q.E.D.
        Proof: <1>1 gives the forward direction and <2>1–<2>3 the reverse, proving (1).

<1>4. Proof of (2): the map $\phi: \mathcal L(\RR^+) \to \mathcal L(\RR^+)$, $E \mapsto f(E)$, is a bijection.
    <2>1. $f: \RR^+ \to \RR^+$, $x \mapsto x^2$, is a bijection with inverse $f^{-1}(y) = \sqrt y$.
        Proof: $x^2$ is strictly increasing on $[0, \infty)$ and surjective onto $[0, \infty)$.
    <2>2. $f$ maps measurable sets to measurable sets.
        Proof: For measurable $E$, $f(E) = (f^{-1})^{-1}(E)$, the preimage of the measurable set $E$ under the continuous map $f^{-1} = \sqrt{\cdot}$; preimages of measurable sets under continuous maps are measurable.
    <2>3. $\phi$ is injective.
        Proof: Since $f$ is injective, $E = f^{-1}(f(E))$ for every $E$; if $f(E_1) = f(E_2)$, then $E_1 = f^{-1}(f(E_1)) = f^{-1}(f(E_2)) = E_2$.
    <2>4. $\phi$ is surjective.
        Proof: For $F \in \mathcal L(\RR^+)$, let $E \definedas f^{-1}(F) = \sqrt F$; $E$ is measurable (continuous preimage), and $f(E) = f(f^{-1}(F)) = F$ by <2>1.
    <2>5. Q.E.D.
        Proof: By <2>2–<2>4, $\phi$ is a well-defined bijection of $\mathcal L(\RR^+)$ onto itself, with inverse $F \mapsto f^{-1}(F)$.
:::
