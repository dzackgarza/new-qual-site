---
card: E-HAT-3.H-2
kind: gap-repair
slice: "8 — Hatcher §3.H proof gaps"
source: "Hatcher, Algebraic Topology, §3.H: Example 3H.3 (tmp/hat/AT.txt 16471–16509), paragraph before Theorem 3H.6 (16797–16822), Theorem 3H.6 (16825–16831), Exercise 2 (16836–16837)"
gaps-closed:
  - "Poincaré duality is invoked for an arbitrary local coefficient system L; that statement is false. Repaired to the twisted duality for the orientation system, Theorem 3H.6, with Example 3H.3 supplying the fundamental class."
review: draft
---

# E-HAT-3.H-2 — repair of the Poincaré duality step

**Exercise** (Hatcher §3.H exercise 2, AT.txt 16836–16837): *Compute the homology groups with local coefficients
$H_n(M; M_{\ZZ})$ for a closed nonorientable surface $M$.*

**Numerical answer of the card is correct and unchanged:** for $M=N_g$ ($g\ge1$),
$H_2(M;M_\ZZ)\cong\ZZ$, $H_1(M;M_\ZZ)\cong\ZZ^{g-1}$, $H_0(M;M_\ZZ)\cong\ZZ_2$, $H_n=0$ for $n\ge3$
(and $H_n=0$ for $n<0$). The card's combinatorial verification with the twisted cellular chain complex
at the end of the solution is right ($d_1(a_i)=-2e^0$, $d_2=0$; note that $d_2(e^2)=0$ because the two
occurrences of each letter $a_i$ in $a_1^2\cdots a_g^2$ receive coefficients $1$ and $w_1(a_i)=-1$).

**The gap.** The step "By Poincaré Duality for manifolds with local coefficients, for any closed
$n$-manifold: $H_k(M;\mathcal L)\cong H^{n-k}(M;\ZZ)$" quotes a theorem that does not exist in that
generality: Poincaré duality with local coefficients needs the coefficient system to be the orientation
system $\widetilde{\ZZ}=M_\ZZ$ (or, in Hatcher's ring-bundle formulation, needs a fundamental class
with local degree $1$). For an arbitrary local system it fails already on the surface at hand.

---

## Repair 1 of 1 — the Poincaré duality step (card lines 36–42)

OLD:
```
::: pf-step
By Poincaré Duality for manifolds with local coefficients, for any closed $n$-manifold:
$$
H_k(M; \mathcal{L}) \cong H^{n-k}(M; \ZZ).
$$
For $n = 2$, this gives $H_k(M; \mathcal{L}) \cong H^{2-k}(M; \ZZ)$.
:::
```

NEW:
```
::: pf-step
Duality must be applied to the *orientation* system, not to an arbitrary one. In the generality stated,
Poincaré duality with local coefficients is false: for $M=N_g$ and $\mathcal{L}=\ZZ$ the trivial
system, $H_2(M;\ZZ)=0$ (Theorem 3.26: $H_n(M;\ZZ)$ is $\ZZ$ for $M$ closed, connected and orientable and $0$ otherwise; Example 3H.3 uses exactly this), whereas $H^0(M;\ZZ)=\ZZ$ because $M$ is connected; so
"$H_k(M;\mathcal L)\cong H^{n-k}(M;\ZZ)$ for any closed $n$-manifold and any local system" fails
already for $k=n=2$. What is true, and all that is used, is the following.

Write $\widetilde{\ZZ}=M_\ZZ$ for the system with fibre $\ZZ$ on which a loop acts by $+1$ or $-1$
according to its orientation character $w_1\colon\pi_1M\to\{\pm1\}$; this is the $\mathcal L$ of the
present computation, and $M$ is closed, connected and nonorientable.

(i) *Fundamental class.* By Example 3H.3 (the exact sequence of the twofold orientable cover
$\widetilde M\to M$): $H_n(M;\widetilde{\ZZ})\approx H_n(\widetilde M)\approx\ZZ$; Hatcher identifies
the resulting class as a fundamental class for the nonorientable manifold $M$. In the paragraph
preceding Theorem 3H.6 he states the version of duality that the cap product with a fundamental class
gives for a bundle of rings $E$, under the assumption "that there exists a fundamental class
$[M]\in H_n(M;E)$ restricting to a generator of $H_n(M,M-\{x\};E)$ for all $x\in M$", and notes that
the class just constructed from $H_n(M;\widetilde{\ZZ})$ can be viewed as such a class — the *pure
imaginary fundamental class* $[M]\in H_n(M;E)$ for $E$ the bundle of rings $\ZZ[i]$ with conjugation
acting by $\omega=w_1$.

(ii) *The duality in the form used.* Cap product with that class is an isomorphism
$$
[M]\frown(-)\colon H^{k}(M;\ZZ)\;\xrightarrow{\ \approx\ }\;H_{n-k}(M;\widetilde{\ZZ})
$$
(Theorem 3H.6, first displayed isomorphism). Replacing $k$ by $n-j$ gives, for all $j$,
$$
H_j(M;\mathcal M_{\ZZ})=H_j(M;\widetilde{\ZZ})\;\cong\;H^{\,n-j}(M;\ZZ).
$$
For the surface $n=2$ this is exactly $H_j(M;\mathcal L)\cong H^{2-j}(M;\ZZ)$, $j=0,1,2$.

(For an *orientable* closed connected $n$-manifold the analogous statement with $\mathcal L=\ZZ$ is ordinary Poincaré duality, Theorem 3.30; the $M$ of this exercise is nonorientable, so Theorem 3H.6 is the applicable form.)
:::
```

### Why this closes the gap

* The false general claim is removed and its failure is exhibited on the very space in question
  ($\mathcal L=\ZZ$ trivial, $k=n=2$), so no step silently assumes more duality than the book proves.
* Every statement used is one of Hatcher's: Example 3H.3 for the existence of the fundamental class in
  $H_n(M;\widetilde{\ZZ})\cong\ZZ$ for closed connected nonorientable $M$, and Theorem 3H.6 for the
  cap-product isomorphism. Theorem 3H.6 applies precisely because $M=N_g$ is a closed, connected,
  nonorientable $n$-manifold, $n=2$.
* The conclusion is *not* weakened: the isomorphism $H_j(M;M_\ZZ)\cong H^{2-j}(M;\ZZ)$ that the rest of
  the card uses is exactly the $j$-th case of the repaired statement, so the computed groups
  $(\ZZ,\ZZ^{g-1},\ZZ_2)$ are unchanged.
