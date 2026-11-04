---
schema: qual/card@1
id: P-UWALG10-6
kind: problem
title: 'Abelian Galois groups make every subextension Galois; $\QQ(\sqrt{1+\sqrt2})$ and its Galois closure'
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-01
  note: >-
    Statement read from the card in `corpus/collections/SRC-UW-ALG-2010`; no correction is claimed.
- event: solution-written
  by: claude
  date: 2026-11-01
  note: >-
    (a) normality of $K/F$ from $\operatorname{Gal}(L/K)\trianglelefteq G$ and the abelian hypothesis,
    which forces $\sigma(K)=K$. (b) $[K:\QQ]=4$ via $\sqrt2=\alpha^2-1$, the non-square norm
    $N(1+\sqrt2)=-1$, and the two non-real conjugates $\pm i\sqrt{\sqrt2-1}$, so $K\subset\RR$ is not
    normal. (c) $L=\QQ(\alpha,i)$ with $[L:\QQ]=8$ and $\operatorname{Gal}(L/\QQ)=\langle v,c\rangle$,
    $v^4=c^2=1$, $cvc=v^{-1}$, i.e. dihedral of order $8$; the eight automorphisms are listed.
    Nothing is left in outline.
---
---

::: {.problem}
(a) Let $L/F$ be a field extension that is finite and Galois.
Show that if the Galois group $\operatorname{Gal}(L/F)$ is abelian then for every intermediate field $F\subseteq K\subseteq L$, $K/F$ is also a Galois extension.

(b) Let $K=\QQ\big(\sqrt{1+\sqrt2}\big)\subset\RR$. Show that $K/\QQ$ is an extension of degree $4$ that is not Galois.

(c) Let $L$ be the smallest Galois extension of $\QQ$ that contains $K=\QQ\big(\sqrt{1+\sqrt2}\big)$. Compute the group $\operatorname{Gal}(L/\QQ)$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Part (a): if $L/F$ is finite Galois with $G=\operatorname{Gal}(L/F)$ abelian, then every intermediate $K$ gives $K/F$ Galois, with $\operatorname{Gal}(K/F)\cong G/\operatorname{Gal}(L/K)$.

::: {.pf-proof}

$K/F$ is separable: $L/F$ is separable, and separability passes to intermediate extensions, since the minimal polynomial over $F$ of an element of $K$ has no repeated roots in $L$.

$K/F$ is normal, that is, $\sigma(K)=K$ for every $F$-embedding $\sigma:K\to\overline F$. Such a $\sigma$ extends to an $F$-embedding $L\to\overline F$ because $L/F$ is algebraic; and since $L/F$ is normal, that extension is an automorphism of $L$, i.e. an element $\sigma\in G$.

Now $K$ is the fixed field of $H=\operatorname{Gal}(L/K)$, by the fundamental theorem of Galois theory. For $\sigma\in G$ and $h\in H$,
$$
\sigma h\sigma^{-1}\in\sigma H\sigma^{-1}=H,
$$
because $G$ is abelian, so $\sigma h\sigma^{-1}$ fixes $K$: for $k\in K$, $\sigma h\sigma^{-1}(k)=\sigma\sigma^{-1}(k)=k$ since $h$ fixes $\sigma^{-1}(k)$ — more directly, $\sigma h\sigma^{-1}\in H$ means it fixes $K$. Hence $\sigma H\sigma^{-1}=H$ for all $\sigma$, and
$$
\sigma(K)=\sigma\bigl(\operatorname{Fix}(H)\bigr)=\operatorname{Fix}(\sigma H\sigma^{-1})=\operatorname{Fix}(H)=K .
$$
So $K/F$ is separable and normal, hence Galois. The group is $G/H$ by the fundamental theorem, and $H\trianglelefteq G$ because $G$ is abelian.

:::

:::

::: {.pf-step #s2}

Part (b): $\alpha=\sqrt{1+\sqrt2}$, $K=\QQ(\alpha)$ has $[K:\QQ]=4$ and satisfies $\alpha^4-2\alpha^2-1=0$.

::: {.pf-proof}

From $\alpha^2=1+\sqrt2$ we get $\sqrt2=\alpha^2-1\in\QQ(\alpha)$, and then
$$
(\alpha^2-1)^2=2,\qquad\text{i.e.}\qquad \alpha^4-2\alpha^2-1=0 .
$$
So $\QQ(\sqrt2)\subseteq K$ and $K=\QQ(\sqrt2)(\alpha)$, where $\alpha$ is a root of $T^2-(1+\sqrt2)\in\QQ(\sqrt2)[T]$.

$1+\sqrt2$ is not a square in $\QQ(\sqrt2)$: the norm $N_{\QQ(\sqrt2)/\QQ}(1+\sqrt2)=1-2=-1$, whereas any square $\beta^2$ has norm $N(\beta)^2\ge0$ in $\QQ$. Hence $T^2-(1+\sqrt2)$ is irreducible over $\QQ(\sqrt2)$, and
$$
[K:\QQ]=[\QQ(\sqrt2):\QQ]\cdot[K:\QQ(\sqrt2)]=2\cdot2=4 .
$$
Consistently, $x^4-2x^2-1$ is the minimal polynomial of $\alpha$ over $\QQ$, of degree $4$.

:::

:::

::: {.pf-step #s3}

Part (b), conclusion: $K/\QQ$ is not Galois.

::: {.pf-proof}

The conjugates of $\alpha$ over $\QQ$ are the roots of $x^4-2x^2-1$. Substituting $y=x^2$ gives $y^2-2y-1=0$, so $y=1\pm\sqrt2$, and the four roots are
$$
\pm\alpha=\pm\sqrt{1+\sqrt2},\qquad \pm\beta:=\pm\sqrt{1-\sqrt2}=\pm i\sqrt{\sqrt2-1}.
$$
Since $\sqrt2-1>0$, the numbers $\pm\beta$ are non-real, while $K=\QQ(\alpha)\subseteq\RR$. So $K$ does not contain all the conjugates of $\alpha$, hence is not normal over $\QQ$; being an extension of characteristic $0$ it is separable, so it is not Galois.

:::

:::

::: {.pf-step #s4}

Part (c): $L=\QQ(\alpha,\beta)=\QQ(\alpha,i)$, of degree $8$ over $\QQ$.

::: {.pf-proof}

$L$ is the splitting field of $x^4-2x^2-1$, hence the smallest Galois extension of $\QQ$ containing $K$.

With $\beta=i\sqrt{\sqrt2-1}$ one has $\alpha\beta=i\sqrt{(1+\sqrt2)(\sqrt2-1)}=i\sqrt{2-1}=\pm i$, so $i\in L$ and $L=\QQ(\alpha,\beta)=\QQ(\alpha,i)$; conversely $\beta=\pm i/\alpha\in\QQ(\alpha,i)$.

Since $K\subseteq\RR$ and $i\notin\RR$, we have $i\notin K$, so $[L:\QQ]=[K:\QQ]\cdot2=8$.

:::

:::

::: {.pf-step #s5}

Part (c), conclusion: $\operatorname{Gal}(L/\QQ)=\langle v,c\rangle$ with $v^4=c^2=1$ and $cvc=v^{-1}$; it is the dihedral group of order $8$.

::: {.pf-proof}

An automorphism $\sigma$ of $L$ is determined by $\sigma(\alpha)$, which must be one of $\pm\alpha,\pm\beta$, and by $\sigma(i)=\pm i$; and $\sigma(\beta)=\sigma(i)/\sigma(\alpha)$ is then forced. This gives at most $4\cdot2=8$ automorphisms, and since $\abs{\operatorname{Gal}(L/\QQ)}=[L:\QQ]=8$, every such choice is an automorphism. They are:

$$
\begin{array}{c|cccc}
 & \alpha & \beta & i\\
\hline
\mathrm{id} & \alpha & \beta & i\\
c & \alpha & -\beta & -i\\
\tau & -\alpha & \beta & -i\\
\tau c & -\alpha & -\beta & i\\
u & \beta & \alpha & i\\
v & \beta & -\alpha & -i\\
w & -\beta & -\alpha & i\\
w' & -\beta & \alpha & -i
\end{array}
$$

In particular $v^2=\tau$ (applying $v$ twice: $\alpha\mapsto\beta\mapsto-\alpha$, $\beta\mapsto-\alpha\mapsto-\beta$, $i\mapsto i$), so $v$ has order $4$; and $c$ has order $2$.

Composing with the table: $v^3$ sends $\alpha\mapsto v^2(\beta)=-\beta$, $\beta\mapsto v^2(-\alpha)=\alpha$ and $i\mapsto-i$, so $v^3=v^{-1}$. On the other hand
$$
cvc(\alpha)=c\bigl(v(\alpha)\bigr)=c(\beta)=-\beta,\qquad
cvc(\beta)=c\bigl(v(-\beta)\bigr)=c(\alpha)=\alpha,\qquad
cvc(i)=c\bigl(v(-i)\bigr)=c(i)=-i,
$$
so $cvc$ agrees with $v^3$ on the generators $\alpha,\beta,i$ of $L$. Hence $cvc=v^{-1}$.

Hence $\operatorname{Gal}(L/\QQ)=\langle v,c\rangle$ is presented by $v^4=c^2=1$, $cvc=v^{-1}$, which is the dihedral group $D_8$ of order $8$. It is non-abelian, consistent with part [](#s1){.pf-ref}: $K$ corresponds to the non-normal subgroup $\langle c\rangle$ or one of its conjugates.

:::

:::

:::

:::
