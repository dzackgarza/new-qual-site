---
schema: qual/card@1
id: P-WROEI
kind: problem
title: Galois group of $x^7-3$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Splitting Fields
  - Roots of Unity
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: solution-reviewed
  by: claude
  date: 2026-11-06
  note: >-
    Rewritten as a Lamport structured proof. What was checked: the statement (a
    computation, no repair needed), and the existing prose solution against a fresh
    re-derivation: x^7 - 3 is Eisenstein at 3, so irreducible of degree 7, and the
    roots are alpha*zeta^k with zeta a primitive 7th root, so the splitting field is
    Q(alpha, zeta); zeta has degree 6 because Phi_7(x+1) is Eisenstein at 7; the
    intersection Q(alpha) cap Q(zeta) has degree dividing both 7 and 6, hence is Q;
    [K:Q] <= 7*6 because the minimal polynomial of alpha over Q(zeta) divides x^7-3,
    and [K:Q] is a multiple of both 7 and 6, hence equals 42; sigma: alpha -> zeta
    alpha fixing zeta exists and has order 7; tau: zeta -> zeta^3 fixing alpha
    exists and has order 6 since 3 generates (Z/7)^x; tau sigma tau^{-1} = sigma^3
    checked on the two generators; and the group is C_7 rtimes C_6 = AGL_1(F_7) of
    order 42. Correct. The prose asserted the coprimality step and the degree 42
    without proof; both are now argued, the second by the bound plus divisibility
    rather than by an unproved multiplicativity. No source solution is retained for
    this card, so no source comparison was made. What was not checked: any printed
    source.
---

::: {.problem}
Compute the Galois group of $p(x) = x^7 - 3$ over $\QQ$.
:::

::: {.solution}
Let $\alpha=\sqrt[7]{3}\in\RR$, let $\zeta$ be a primitive $7$th root of unity, and put $K=\QQ(\alpha,\zeta)$.

::: pf

::: {.pf-step #roots}
$x^7-3$ is irreducible over $\QQ$, $[\QQ(\alpha):\QQ]=7$, its roots in $\CC$ are $\alpha\zeta^k$ for $0\leq k\leq6$, and $K$ is its splitting field.

::: pf-proof
$x^7-3$ is Eisenstein at the prime $3$: the leading coefficient is not divisible by $3$, every other coefficient is divisible by $3$, and the constant term $-3$ is not divisible by $9$. So it is irreducible, hence is the minimal polynomial of $\alpha$ and $[\QQ(\alpha):\QQ]=7$. The roots of $x^7=3$ are $\alpha\zeta^k$, $0\leq k\leq6$, because $(\alpha\zeta^k)^7=\alpha^7\zeta^{7k}=3$, and there are seven of them, a nonzero polynomial of degree seven having at most seven roots in $\CC$. These roots all lie in $\QQ(\alpha,\zeta)$ and generate it over $\QQ$, since $\alpha$ is the root with $k=0$ and $\zeta=\alpha\zeta/\alpha$ is a quotient of two roots; so $K$ is the splitting field.
:::

:::

::: {.pf-step #degree}
$[K:\QQ]=42$, $[K:\QQ(\zeta)]=7$ and $[K:\QQ(\alpha)]=6$.

::: pf-proof
$[\QQ(\zeta):\QQ]=6$: $\zeta$ is a root of $\Phi_7=x^6+x^5+\cdots+x+1$, and $\Phi_7(x+1)=((x+1)^7-1)/x=x^6+7x^5+\cdots+7$ is Eisenstein at $7$, so $\Phi_7$ is irreducible and is the minimal polynomial of $\zeta$. Hence $[K:\QQ]=[K:\QQ(\zeta)]\cdot6$.

The intersection $\QQ(\alpha)\cap\QQ(\zeta)$ has degree over $\QQ$ dividing both $7$ and $6$, by the tower law applied to $\QQ\subseteq\QQ(\alpha)\cap\QQ(\zeta)\subseteq\QQ(\alpha)$ and to $\QQ\subseteq\QQ(\alpha)\cap\QQ(\zeta)\subseteq\QQ(\zeta)$; as $\gcd(7,6)=1$ that degree is $1$.

Now $K=\QQ(\zeta)(\alpha)$, so $[K:\QQ(\zeta)]$ is the degree of the minimal polynomial of $\alpha$ over $\QQ(\zeta)$, which divides $x^7-3$ and is therefore at most $7$; hence $[K:\QQ]=[K:\QQ(\zeta)]\cdot6\leq42$. By the tower law $[K:\QQ]=[K:\QQ(\alpha)]\cdot7$ is a multiple of $7$, and by the display it is a multiple of $6$; since $7$ and $6$ are coprime it is a multiple of $42$. Therefore $[K:\QQ]=42$, and then $[K:\QQ(\zeta)]=7$ and $[K:\QQ(\alpha)]=6$.
:::

:::

::: {.pf-step #sigma}
There is a $\QQ$-automorphism $\sigma$ of $K$ with $\sigma(\alpha)=\zeta\alpha$ and $\sigma(\zeta)=\zeta$, and it has order $7$.

::: pf-proof
By step [](#degree){.pf-ref} $[\QQ(\alpha,\zeta):\QQ(\zeta)]=7$, which is the degree of $x^7-3$, so this polynomial remains irreducible over $\QQ(\zeta)$; both $\alpha$ and $\zeta\alpha$ are roots of it. For an irreducible polynomial over a field, the assignment of one root to another extends to an isomorphism of the simple extensions fixing the base field, so there is a $\QQ(\zeta)$-automorphism $\sigma$ of $K$ with $\sigma(\alpha)=\zeta\alpha$ and $\sigma(\zeta)=\zeta$. Then $\sigma^k(\alpha)=\zeta^k\alpha$ and $\sigma^k(\zeta)=\zeta$, so $\sigma^7=\mathrm{id}$ and $\sigma^k\neq\mathrm{id}$ for $1\leq k\leq6$ because $\zeta^k\alpha\neq\alpha$. Hence the order is $7$.
:::

:::

::: {.pf-step #tau}
There is a $\QQ$-automorphism $\tau$ of $K$ with $\tau(\alpha)=\alpha$ and $\tau(\zeta)=\zeta^3$, and it has order $6$.

::: pf-proof
By step [](#degree){.pf-ref} $[\QQ(\alpha,\zeta):\QQ(\alpha)]=6$, which is the degree of $\Phi_7$, so $\Phi_7$ is irreducible over $\QQ(\alpha)$; both $\zeta$ and $\zeta^3$ are roots of $\Phi_7$, being primitive $7$th roots of unity. As in the previous step, the assignment extends to a $\QQ(\alpha)$-automorphism $\tau$ of $K$. The powers of $3$ modulo $7$ are $3,2,6,4,5,1$, so $\tau^k(\zeta)=\zeta^{3^k}$ equals $\zeta$ exactly when $3^k\equiv1\pmod 7$, first at $k=6$; hence the order of $\tau$ is $6$.
:::

:::

::: {.pf-step #relation}
$\tau\sigma\tau^{-1}=\sigma^3$, and $\Gal(K/\QQ)=\generators{\sigma,\tau}$.

::: pf-proof
Both sides fix $\QQ$. On $\alpha$: using $\tau^{-1}(\alpha)=\alpha$, we get $\tau\sigma\tau^{-1}(\alpha)=\tau(\zeta\alpha)=\zeta^3\alpha=\sigma^3(\alpha)$; and $\sigma^3(\zeta)=\zeta=\tau\sigma\tau^{-1}(\zeta)$. Since $K$ is generated by $\alpha$ and $\zeta$, the two automorphisms agree everywhere, giving the relation.

The subgroup $\generators{\sigma,\tau}$ of $\Gal(K/\QQ)$ contains $\generators{\sigma}$ of order $7$ and $\generators{\tau}$ of order $6$; their intersection is trivial because its order divides both $7$ and $6$, so the subgroup has order $42$. But $|\Gal(K/\QQ)|=[K:\QQ]=42$ by step [](#degree){.pf-ref} and the normality and separability of a splitting field of a separable polynomial, so the subgroup is the whole group.
:::

:::

::: {.pf-step}
$\Gal(K/\QQ)\cong C_7\rtimes C_6\cong\operatorname{AGL}_1(\FF_7)$, the Frobenius group of order $42$.

::: pf-proof
By step [](#relation){.pf-ref} the group is generated by $\sigma$ of order $7$ and $\tau$ of order $6$ subject to $\tau\sigma\tau^{-1}=\sigma^3$, which is the semidirect product of $\generators{\sigma}\cong C_7$ (normal, being of index $6$ and of prime order $7$) by $\generators{\tau}\cong C_6$, the action being $3\mapsto$ conjugation, faithful because $3$ generates $(\ZZ/7\ZZ)^\times$. Concretely, on the affine line $\FF_7$ the maps $x\mapsto x+1$ and $x\mapsto 3x$ generate the group of all $x\mapsto ax+b$ with $a\in\FF_7^\times$, $b\in\FF_7$, which has $6\cdot7=42$ elements; that group is $\operatorname{AGL}_1(\FF_7)$, and the resulting isomorphism $C_7\rtimes C_6\to\operatorname{AGL}_1(\FF_7)$ is the standard one sending $\sigma$ to translation and $\tau$ to scaling.
:::

:::

:::
:::
