# Schwarz

## Hyperbolic Translations / Blaschke Factors

:::{.definition title="Hyperbolic translations/Blaschke factors"}
For $a\in \DD$, the maps
\[
\psi_a \da {a-z\over 1-\bar{a}z}
\]
are *hyperbolic translations* because they preserve the hyperbolic metric on the Poincaré disc.
They're also commonly called **Blaschke factors**, and also sometimes taken to be
\[
\phi_a \da {z-a \over 1-\bar{a} z} = - \psi_a
.\]
A rational map of the form
\[
\Psi_{\vector a}(z) = \lambda \prod_{1\leq k\leq n} \psi_a(z) = \lambda \prod_{1\leq k \leq n} {a_i - z\over 1 - \bar{a_i} z},\qquad \vector a\da\tv{a_1,\cdots, a_n}
\]
with zeros $a_i \in \DD$ is called a **Blaschke product** and is a map $\DD\to \DD$ that preserves $S^1$.
:::

:::{.proposition title="Properties of hyperbolic translations / Blaschke factors"}
Some useful properties:

- $\psi_a \in \Aut(\DD)$
- $\psi_a(S^1) = S^1$
- $\psi_a(0) = a$ and $\psi(a) = 0$
- With this choice of sign, $\psi_{a} \inv = \psi_{a}$, so $\psi_a^2 = \id$.
- $\psi_a'(z) = {\abs{a}^2 - 1 \over \qty{1-\bar{a} z}^2 }$
- $\psi_a(\lambda z) = \lambda\psi_{\bar\lambda a}(z)$
:::

:::{.proof title="of properties"}
Inverting: set $f(z) = w$ and solve for $z$:
\[
{a-z \over 1 - \bar{a}z} &= w \\
\implies a-z - w(1-\bar{a} z) &= 0 \\
\implies z&= {w-a \over \bar a w - 1} = {a-w\over 1-\bar a w}
.\]

Differentiating: the quotient rule
\[
\psi'_a(z) 
= {-(1-\bar a z) + \bar a(a-z) \over \qty{1-\bar a z}^2}
= {-1 + \abs{a}^2 \over \qty{1-\bar a z}^2}
.\]

Scaling: use a fun trick, insert $1=\bar\lambda \lambda$ like so
\[
\psi_a(\lambda z)
&=
{a - \lambda z \over 1 - \bar a \lambda z}\\
&=
{\lambda\bar\lambda a - \lambda z \over 1 - \bar a \lambda z} \\
&= \lambda {\bar\lambda a - z \over 1 - \bar{\bar\lambda a} z} \\
&= \lambda \psi_{\bar \lambda a}(z)
.\]

Being an involution: check $\psi_a(\psi_a(z))$ satisfies the Schwarz lemma and has two fixed points, forcing it to be the identity.
:::

:::{.theorem title="Structure theorem: automorphisms of the disc"}
Every map $g\in \Aut(\DD)$ is of the form 

\[
\Aut(\DD) = \ts{ \lambda \psi_a(z) \st a\in \DD, \lambda \in S^1 }
,\]
i.e. they are all Blaschke factors and rotations.
:::

:::{.proof title="of theorem, sketch"}

- That these maps are biholomorphisms: they're compositions of $z\mapsto \lambda z$ and $z\mapsto {z-a\over 1-\bar a z}$, which are biholomorphisms.
- Let $f \in \BiHol(\Delta)$ be arbitrary, fix $a\in \Delta$ with $f(a) = 0$
- Write $M(z) = {z-a\over 1-\bar a z}$, then note that $M(a) = 0$ and this is a biholomorphism.
- $g\da f\circ M\inv \in \BiHol(\Delta)$ sends $0\to0$ and is thus a rotation, so $g(z) = \lambda z$.
- Write $g\circ M = f \circ M \circ M\inv = f$, which exhibits $f$ in the desired form.

- Claim: this representation is unique.
  Consider $f'(z)$, this determines $\Arg(\lambda)$.
:::

## The Schwarz Lemma

:::{.theorem title="Schwarz Lemma" ref="SchwarzzLemma"}
If $f: \DD \to \DD$ is holomorphic with $f(0) = 0$, then

1. $\abs{f(z)} \leq \abs z$ for all $z\in \DD$
2. $\abs{f'(0)} \leq 1$.

Moreover, if 

- $\abs{f(z_0)} = \abs{z_0}$ for any $z_0\in \DD\smz$, or 
- $\abs{f'(0)} = 1$, 

then $f$ is a rotation, i.e. $f(z) = \lambda z$ for some $\abs{\lambda} = 1$.
:::

:::{.theorem title="Schwarz lemma, a useful alternative statement"}
Let $f:\DD\to \DD$ be holomorphic with $f(0) = 0$. 
Then either

- $f(z) = e^{i\theta}z$ is a rotation, or
- $\abs{f'(0)} < 1$ and $\abs{f(z)} < \abs{z}$ for all $z\in \DD$, noting the strict inequalities.

:::

:::{.proof title="of Schwarz"}
\envlist

- Idea: apply the maximum modulus principle to $g(z) \da f(z)/z$.
- $\abs{g(z)} \leq 1$:
  - Expand $f$ at $z=0$ as $\sum_{k\geq 0} c_k z^k$.
    Since $f(0) = c_0$, we have $c_0 = 0$.
  - So $g(z) \da f(z)/z$ is holomorphic on $\DD$, since the singularity at $z=0$ is removable.
  - Set $\abs{z} = r < 1$, then $\abs{g(z)} = \abs{f(z)}/r \leq 1/r$ since $\abs{f(z)} \leq 1$.
  - By MMP, $\abs{g(z)} \leq 1/r$ holds in the entire disc $\abs{z} \leq r$, so take $r\to 1$ to get $\abs{g(z)} \leq 1$
- $\abs{f'(0)} \leq 1$ with equality iff $f$ is a rotation:
  - Note that $f(0) = 0$, so we can write $g(0) = \lim_{z\to 0} {f(z) - f(0) \over z-0} \da f'(0)$.
  - So $1 = \abs{f'(0)} = \abs{g(0)}$.
  - But $\abs{g(z)} \leq 1$ on $\DD$ and $g(z) = 1$ in the interior, so by MMP this makes $g$ constant.
  - So again $f(z) = cz$ with $\abs{c} = 1$.
- $\abs{f(z_0)} = \abs{z_0}\implies f$ is a rotation:
  - Again $\abs{g(z)} \leq 1$, but $\abs{f(z_0)} = \abs{z_0} \implies \abs{g(z_0)} = 1$, so $g$ attains a maximum on $\abs{z}\leq 1$, making it constant, so $f(z) = cz$.
  - Then $\abs{z_0} = \abs{f(z_0)} = \abs{cz_0}$ since $f(z_0) = z_0$, so $\abs{c} = 1$ and $c = e^{i\theta}$ for some $\theta$.
:::

:::{.proof title="of Schwarz, alternative"}


![](figures/2021-12-14_16-30-35.png)

![](figures/2021-12-14_16-30-46.png)

:::

# Exercises

## Blaschke Factors

[[E-IQHNA]]



## Schwarz-Fu

[[E-ZWG4Q]]

[[E-F5K2X]]

[[E-B3YJ4]]

[[E-IU7YG]]

[[E-WHOLO]]

[[E-N4FPI]]

[[E-WUXER]]

[[E-O6K36]]

[[E-DCDFB]]

[[E-GGP77]]

## Estimating

[[E-S4L2M]]

[[E-JLDSM]]

[[E-TMMGS]]

[[E-4OPGJ]]

[[E-VDBOL]]

[[E-2DO4D]]

[[E-NH6D2]]


