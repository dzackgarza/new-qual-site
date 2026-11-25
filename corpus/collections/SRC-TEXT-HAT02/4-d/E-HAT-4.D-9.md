---
schema: qual/card@1
id: E-HAT-4.D-9
kind: problem
title: Diagonal inclusion factors up to homotopy through multiplication
classification:
  areas:
  - topology
  topics:
  - Fiber Bundles
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.D, Exercise 9; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Read against Hatcher, Exercise 9 of §4.D, printed p. 447. The mathematics is right: for the
    unitary case $\operatorname{diag}(z,w)=\operatorname{diag}(zw,1)\operatorname{diag}(w^{-1},w)$
    and the second factor is a loop in $SU(2)\cong S^3$, nullhomotopic, which gives a homotopy
    natural in $(z,w)$ to $\operatorname{diag}(zw,1)$ and, iterated, to
    $\operatorname{diag}(z_1\cdots z_n,1,\dots,1)$; the symplectic case is the same with
    $Sp(1)^n=(S^3)^n$ and $q\mapsto\operatorname{diag}(q^{-1},q)$ nullhomotopic because its class in
    $\pi_3(Sp(2))\cong\ZZ$ is $-1+1$. One citation repaired: the card attributed
    $\pi_3(Sp(n))\cong\ZZ$ and its generation by the block inclusion to 'Exercise 10(b) in §3.C',
    which is the quaternionic-polynomial exercise and says no such thing. The step now cites the
    bundle $S^3=Sp(1)\to Sp(2)\to S^7$ for $\pi_3(S^3)\cong\pi_3(Sp(2))$, Corollary 4.25
    (printed p. 361) for $\pi_3(S^3)\cong\ZZ$, and the conjugate block inclusions for the sign.
    Nothing else changed. Not claimed: a published solution, and no certificate.
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    The card stood in queue D: its solution was prose with no numbered step. It is now a `pf`
    with six steps, three for each of the two cases, each carrying a `pf-proof`; both claims are
    unchanged and the homotopies are the ones the prose had. Cited by number only: Example 1.14
    for $SU(2)\cong S^3$, Corollary 4.25 for $\pi_3(S^3)\cong\ZZ$, and the exact homotopy
    sequence of the bundle $S^3=Sp(1)\to Sp(2)\to S^7$. Checked: the entrywise product identity
    in the complex and in the quaternionic case, that the second factor lies in $SU(2)$ and is a
    loop, that the two block inclusions of $Sp(1)$ in $Sp(2)$ are conjugate — the conjugating element lying in a path component, $Sp(2)$ being path connected — and so induce the
    same isomorphism on $\pi_3$, and that the two classes $-1$ and $+1$ sum to zero.
- event: solution-reviewed
  by: claude
  date: 2026-11-22
  note: >-
    Read against Hatcher, §4.D Exercise 9. A provenance record is added, the card having carried
    none: no retained solution set covers the exercise. The argument reads correct; two items are
    recorded for a further pass — the citation "Example 1.14" in the dated event is wrong, since
    §1.1's 1.14 is a proposition, and the injectivity argument for $\pi_3$ needs $\pi_4(S^7)=0$.
- event: solution-reviewed
  by: claude
  date: 2026-11-22
  note: >-
    Three corrections, from a referee report. (1) The identification of $SU(2)$ with $S^3$ was
    attributed to a proposition of §1.1, which does not state it; it now comes from the bundle
    $SU(1)\to SU(2)\to S^3$ of Corollary 4D.3's proof, whose fibre is the trivial group. (2) The
    false clause "factors through $\CP^1$" is removed. (3) In the $Sp(2)$ step the vanishing needed
    for $\pi_3(Sp(1))\cong\pi_3(Sp(2))$ is $\pi_3(S^7)=\pi_4(S^7)=0$, not $\pi_2(S^7)=0$, and
    both come from Corollary 4.9; and the conjugate block inclusions induce the same map only up to
    the path component of the conjugating element, so path-connectedness of $Sp(2)$ is now said.
---

::: {.problem}
Show that the inclusion $T^n \hookrightarrow U(n)$ of the $n$-torus of diagonal matrices is homotopic to the map $T^n \to U(1) \hookrightarrow U(n)$ sending an $n$-tuple of unit complex numbers $(z_1, \ldots, z_n)$ to the $1 \times 1$ matrix $(z_1 \cdots z_n)$.
Do the same for the diagonal subgroup of $Sp(n)$.
[Hint: Diagonal matrices in $U(n)$ are compositions of scalar multiplication in $n$ lines in $\CC^n$, and $\CP^{n-1}$ is connected.]
:::

::: {.solution}
No retained solution set covers this exercise: Sam's set ends at §4.3, Koukpari's §4.D heading carries no solutions, and Proudfoot's sheets are §4.1 and §4.2. The argument is the card's own.


Throughout, $\operatorname{diag}(a,b)$ is the diagonal matrix with the displayed entries in the first two slots.

::: pf

::: pf-step
For diagonal entries $z,w$ of modulus $1$,
$$
\operatorname{diag}(z,w)=\operatorname{diag}(zw,1)\operatorname{diag}(w^{-1},w),
$$
and the second factor is a loop in $SU(2)\cong S^3$, hence nullhomotopic.

::: pf-proof
Multiplying the two diagonal matrices entrywise gives diagonal entries $(zw)(w^{-1})=z$ and $1\cdot w=w$. The second factor has determinant $w^{-1}w=1$ and unitary diagonal entries, so it lies in $SU(2)$. The group $SU(2)$ is $S^3$: the bundle $SU(1)\to SU(2)\to S^3$ of Corollary 4D.3's proof, which is the case $n=2$ of $SU(n-1)\to SU(n)\to S^{2n-1}$, has contractible fibre $SU(1)=\{1\}$, so its total space is homeomorphic to $S^3$. Hence it is simply connected and every loop in it is nullhomotopic, in particular the loop $w\mapsto\operatorname{diag}(w^{-1},w)$, which is the composite of $w\mapsto(w^{-1},w)$ with the diagonal inclusion $S^1\times S^1\to SU(2)$.
:::

:::

::: pf-step
Multiplying a chosen nullhomotopy of the second factor by $\operatorname{diag}(zw,1)$ gives a homotopy, natural in $(z,w)$, from $\operatorname{diag}(z,w)$ to $\operatorname{diag}(zw,1)$.

::: pf-proof
Let $H:S^1\times I\to SU(2)$ run from $H(w,0)=\operatorname{diag}(w^{-1},w)$ to $H(w,1)=I_2$. Then $(z,w,t)\mapsto\operatorname{diag}(zw,1)H(w,t)$ is continuous in all three variables, starts at $\operatorname{diag}(z,w)$ by step 1 and ends at $\operatorname{diag}(zw,1)$. Both endpoints depend continuously on $(z,w)$, so the homotopy is natural in the pair.
:::

:::

::: pf-step
Iterating step 2 over adjacent entries,
$$
\operatorname{diag}(z_1,\dots,z_n)\simeq\operatorname{diag}(z_1\cdots z_n,1,\dots,1),
$$
so the diagonal inclusion $T^n\hookrightarrow U(n)$ is homotopic to $T^n\xrightarrow{(z_i)\mapsto\prod z_i}U(1)\hookrightarrow U(n)$.

::: pf-proof
Applying step 2 to the first two entries replaces $(z_1,z_2,z_3,\dots)$ by $(z_1z_2,1,z_3,\dots)$ and leaves the other entries alone, since the homotopy only touches the first two slots; repeating it $n-1$ times moves the product of all entries into the first slot. A composite of finitely many homotopies is a homotopy, so the diagonal inclusion is homotopic to the map sending $(z_i)$ to $\operatorname{diag}(\prod z_i,1,\dots,1)$, which is exactly the composite of $(z_i)\mapsto\prod z_i$ with the block inclusion $U(1)\hookrightarrow U(n)$.
:::

:::

::: pf-step
For $Sp(n)$ the diagonal subgroup is $Sp(1)^n=(S^3)^n$, and the same reduction begins with
$$
\operatorname{diag}(q_1,q_2)=\operatorname{diag}(q_1q_2,1)\operatorname{diag}(q_2^{-1},q_2).
$$

::: pf-proof
$Sp(n)$ is the group of quaternionic matrices preserving the standard Hermitian form; its diagonal matrices have entries of quaternionic modulus $1$, that is elements of $Sp(1)\cong S^3$, so the diagonal subgroup is $(S^3)^n$. The displayed identity is verified entrywise as in step 1, in the associative algebra $\HH$: the first diagonal entry is $(q_1q_2)(q_2^{-1})=q_1$ and the second is $1\cdot q_2=q_2$.
:::

:::

::: pf-step
The map $S^3\to Sp(2)$, $q\mapsto\operatorname{diag}(q^{-1},q)$, is nullhomotopic, because $\pi_3(Sp(2))\cong\ZZ$ and the two diagonal blocks represent $-1$ and $+1$, which sum to zero.

::: pf-proof
The unit sphere bundle of $\HH^2$ is $S^3=Sp(1)\to Sp(2)\to S^7$, and its exact homotopy sequence gives $\pi_3(Sp(1))\cong\pi_3(Sp(2))$: the two groups that must vanish are $\pi_4(S^7)$ and $\pi_3(S^7)$, both of which are $0$ by Corollary 4.9 since $3,4<7$; Corollary 4.25 gives $\pi_3(S^3)\cong\ZZ$, so $\pi_3(Sp(2))\cong\ZZ$. The block inclusions $q\mapsto\operatorname{diag}(q,1)$ and $q\mapsto\operatorname{diag}(1,q)$ are conjugate by the swap matrix, which lies in $Sp(2)$, and conjugation by a fixed element of a topological group is homotopic to the identity through multiplication, so the two induce the same isomorphism of $\pi_3$. With the first block giving the generator $+1$, the second gives $+1$ as well, and the map $q\mapsto\operatorname{diag}(q^{-1},q)$ is the sum of the classes of $q\mapsto\operatorname{diag}(q^{-1},1)$ and $q\mapsto\operatorname{diag}(1,q)$, that is $-1+1=0$, because inversion of $Sp(1)$ acts as $-1$ on $\pi_3(S^3)$. A map whose class in $\pi_3$ vanishes is nullhomotopic.
:::

:::

::: pf-step
Iterating gives
$$
\operatorname{diag}(q_1,\dots,q_n)\simeq\operatorname{diag}(q_1\cdots q_n,1,\dots,1),
$$
so the diagonal inclusion $Sp(1)^n\hookrightarrow Sp(n)$ is homotopic to the composite through $Sp(1)$.

::: pf-proof
The homotopy of step 5 is natural in the pair $(q_1,q_2)$, exactly as in step 2 with $H$ replaced by a nullhomotopy of $q\mapsto\operatorname{diag}(q^{-1},q)$ inside $Sp(2)$, so it may be applied to adjacent entries and iterated, moving the product of the entries into the first slot. The result is a homotopy from the diagonal inclusion to $(q_i)\mapsto\operatorname{diag}(\prod q_i,1,\dots,1)$, which is the composite of $(q_i)\mapsto\prod q_i$ with the block inclusion $Sp(1)\hookrightarrow Sp(n)$.
:::

:::

:::
:::
