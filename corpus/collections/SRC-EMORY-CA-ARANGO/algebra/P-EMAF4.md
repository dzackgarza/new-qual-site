---
schema: qual/card@1
id: P-EMAF4
kind: problem
title: "Galois extensions and splitting fields over Q"
classification:
  areas:
  - algebra
  topics:
  - Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared Fields 4 on PDF page 2; retained this card's already-correct quartic in place of the source's erroneous leading exponent."
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Constructed and iterated the quartic automorphism, justified both splitting-field and degree arguments, and checked the faithful cubic root action and strictness of the quadratic subextension."
---

::: problem
(a) Show that $\sqrt{2 + \sqrt{2}}$ is a root of $p(x) = x^4 - 4x^2 + 2 \in \mathbf{Q}[x]$.

(b) Prove that $\mathbf{Q}(\sqrt{2 + \sqrt{2}})$ is a Galois extension of $\mathbf{Q}$ and find its Galois group.

(c) Let $f(x) = x^3 - 5$.
Determine the splitting field $K$ of $f(x)$ over $\mathbf{Q}$ and the Galois group of $f(x)$.
Give an example of a proper sub-extension $\mathbf{Q} \subset L \subset K$ such that $L/\mathbf{Q}$ is Galois.
:::

::: {.solution}
**Part (a).**

<1>1. Let $\alpha = \sqrt{2 + \sqrt{2}}$; then $\alpha^2 = 2 + \sqrt{2}$, so $(\alpha^2 - 2)^2 = 2$.
::: {.proof}
square both sides.
:::

<1>2. Hence $\alpha^4 - 4\alpha^2 + 4 = 2$, i.e. $\alpha^4 - 4\alpha^2 + 2 = 0$.
::: {.proof}
expand $(\alpha^2 - 2)^2 = \alpha^4 - 4\alpha^2 + 4 = 2$.
:::

<1>3. Therefore $\alpha$ is a root of $p(x) = x^4 - 4x^2 + 2$.
::: {.proof}
<1>2.
:::

**Part (b).**

<1>1. The roots of $p(x) = x^4 - 4x^2 + 2$ are $\pm\sqrt{2 \pm \sqrt{2}}$.
::: {.proof}
solve $x^2 = 2 \pm \sqrt{2}$.
:::

<1>2. $\QQ(\sqrt{2 + \sqrt{2}})$ contains all four roots.
::: {.proof}
$\sqrt{2 - \sqrt{2}} = \frac{\sqrt{2}}{\sqrt{2 + \sqrt{2}}}$, and $\sqrt{2} = (\sqrt{2+\sqrt{2}})^2 - 2 \in \QQ(\sqrt{2+\sqrt{2}})$, so $\sqrt{2 - \sqrt{2}} \in \QQ(\sqrt{2+\sqrt{2}})$; hence all four roots $\pm\sqrt{2 \pm \sqrt{2}}$ lie in $\QQ(\sqrt{2+\sqrt{2}})$.
:::

<1>3. Hence $\QQ(\sqrt{2+\sqrt{2}})$ is the splitting field of $p$, so it is Galois over $\QQ$.
::: {.proof}
All the roots belong to this field by <1>2, and one
of them generates it over $\QQ$, so it is precisely
the splitting field. The four roots are distinct.
A splitting field of a separable polynomial is
Galois [@DF04].
:::

<1>4. The polynomial $p$ is irreducible over $\QQ$.
::: {.proof}
Eisenstein's criterion at $2$ applies directly to
$p(x)=x^4-4x^2+2$: two divides every nonleading
coefficient, and four does not divide the constant
coefficient [@DF04].
:::

<1>5. Hence $[\QQ(\sqrt{2+\sqrt{2}}) : \QQ] = 4$, and $\operatorname{Gal} = \ZZ/4$.
::: {.proof}
Put $\beta=\sqrt{2-\sqrt2}$ and $E=\QQ(\alpha)$.
Irreducibility gives $[E:\QQ]=4$. Sending $\alpha$
to the root $\beta$ of its minimal polynomial
defines a $\QQ$-embedding $\sigma:E\to E$.
It is onto, since an injective endomorphism of
the finite-dimensional rational vector space $E$
is surjective. It is therefore an automorphism.

The identities $\sqrt2=\alpha^2-2$ and
$\beta=\sqrt2/\alpha$ give
$$
\sigma(\sqrt2)=\beta^2-2=-\sqrt2,
\qquad \sigma(\beta)=-\sqrt2/\beta=-\alpha.
$$
Thus its action on the roots is the four-cycle
$\alpha\mapsto\beta\mapsto-\alpha\mapsto-\beta
\mapsto\alpha$. Its order is exactly four.
The Galois group has order $[E:\QQ]=4$ [@DF04],
so these four powers exhaust it, proving cyclicity.
:::

**Part (c).**

<1>1. The roots of $x^3 - 5$ are $\sqrt[3]{5}, \sqrt[3]{5}\omega, \sqrt[3]{5}\omega^2$, where $\omega$ is a primitive cube root of unity.
::: {.proof}
the cube roots of $5$.
:::

<1>2. The splitting field is $K = \QQ(\sqrt[3]{5}, \omega)$.
::: {.proof}
All three roots lie in the displayed field.
Conversely, their field contains $\sqrt[3]{5}$
and the ratio $(\sqrt[3]{5}\omega)/\sqrt[3]{5}=\omega$.
This proves equality with the splitting field.
:::

<1>3. $[K : \QQ] = 6$, and $\operatorname{Gal}(K/\QQ) \cong S_3$.
::: {.proof}
Eisenstein's criterion at five gives
$[\QQ(\sqrt[3]{5}):\QQ]=3$ [@DF04]. This field
is real, whereas $\omega$ is nonreal and satisfies
$x^2+x+1=0$. Adjoining $\omega$ therefore has
degree two, and the tower law gives $[K:\QQ]=6$.
The extension is Galois as a splitting field in
characteristic zero. Its automorphisms permute
the three roots faithfully, since these roots
generate $K$. Its group of order six therefore
embeds into $S_3$ of order six and equals the
full symmetric group on the roots.
:::

<1>4. A proper Galois sub-extension is $L = \QQ(\omega)$.
::: {.proof}
The field $\QQ(\omega)$ is the splitting field
of $x^2+x+1$, with distinct nonreal roots
$\omega,\omega^2$. It is a degree-two Galois
extension, with group $\ZZ/2$ [@DF04].
Since $1<2<6=[K:\QQ]$, both inclusions
$\QQ\subsetneq\QQ(\omega)\subsetneq K$ are strict.
:::

<1>5. Q.E.D.
::: {.proof}
<1>3 (a), <1>5 (b), and <1>3–<1>4 (c).
:::
:::
