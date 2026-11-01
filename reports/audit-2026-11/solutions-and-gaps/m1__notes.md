# E-SS3.PR-5 — solution delivered, with two corrections to the book's wording

Slice 2 of swarm `smvy31u3e` (member m1). Nothing under `corpus/` was touched.

## What to install

* `solution-block.md` — the complete `::: {.solution}` … `:::` block, ready to append verbatim to
  `corpus/collections/SRC-TEXT-SS03/ch3-problems/E-SS3.PR-5.md` (append after the closing `:::` of
  the `.exercise` div; the card already ends with a blank line).
* Optionally record the authoring in the card's front matter, e.g.
  ```yaml
  - event: solution-written
    by: <installer>
    date: <date>
    note: >-
      (a) holomorphy, O(1/|z|) decay and the jump proved via the Poisson-kernel convolution;
      (b) Plemelj formula and uniform boundary values under a Hölder condition, and the
      characterisation via the symmetry principle, the maximum modulus principle, Riemann's
      removable-singularity theorem and Liouville. The endpoint cases x = ±M are treated
      explicitly; see the remarks at the end of the block.
  ```

Verified mechanically: the card with the block appended parses and builds under the repo's own
tool `qualc` (`.venv`: Python 3.14, pandoc), in a throwaway root containing only this card:

```
PYTHONPATH=tools ./.venv/bin/python -m qualc build --root <scratch root>   # "1 cards and 4 wiki pages OK"
```

The parse reports sections `['problem', 'solution']`, 357 math elements (31 display), 6 citations
resolved to `[StSh03a]`, and no raw-TeX regressions.

## The book text this slice belongs to

Stein–Shakarchi, *Complex Analysis*, Chapter 3, §9 ("Problems"), problem 5\*, printed page **110**
(PDF page 129 = printed + 19), extracted with

```
pdftotext -layout -f 129 -l 129 assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf out.txt
```

The printed statement (OCR cleaned; displayed formulas restored):

> **5.\*** Let
> $$g(z)=\frac{1}{2\pi i}\int_{-M}^{M}\frac{h(x)}{x-z}\,dx$$
> where $h$ is continuous and supported in $[-M,M]$.
>
> (a) Prove that the function $g$ is holomorphic in $\mathbb{C}-[-M,M]$, and vanishes at infinity, that is, $\lim_{|z|\to\infty}|g(z)|=0$. Moreover, the "jump" of $g$ across $[-M,M]$ is $h$, that is,
> $$h(x)=\lim_{\epsilon\to0,\ \epsilon>0}g(x+i\epsilon)-g(x-i\epsilon).$$
> [Hint: Express the difference $g(x+i\epsilon)-g(x-i\epsilon)$ in terms of a convolution of $h$ with the Poisson kernel.]
>
> (b) If $h$ satisfies a mild smoothness condition, for instance a Hölder condition with exponent $\alpha$, that is, $|h(x)-h(y)|\le C|x-y|^{\alpha}$ for some $C>0$ and all $x,y\in[-M,M]$, then $g(x+i\epsilon)$ and $g(x-i\epsilon)$ converge uniformly to functions $g^{+}(x)$ and $g^{-}(x)$ as $\epsilon\to0$. Then, $g$ can be characterized as the unique holomorphic function that satisfies:
> (i) $g$ is holomorphic outside $[-M,M]$, (ii) $g$ vanishes at infinity, (iii) $g(x+i\epsilon)$ and $g(x-i\epsilon)$ converge uniformly as $\epsilon\to0$ to functions $g^{+}(x)$ and $g^{-}(x)$ with $g^{+}(x)-g^{-}(x)=h(x)$.
> [Hint: If $G$ is another function satisfying these conditions, $g-G$ is entire.]

The card `E-SS3.PR-5.md` matches this transcription (statement, hypotheses, hints, the star), so
the problem asked for is exactly the printed one.

## Book results cited in the block (all read in the extracted text, numbering checked)

| Citation | Statement used |
| --- | --- |
| Ch. 2, Theorem 5.4 | $F(z,s)$ holomorphic in $z$, jointly continuous ⇒ $\int_0^1F(z,s)ds$ holomorphic (used for holomorphy of $g$) |
| Ch. 2, Theorem 5.5 | Symmetry principle: $f^{\pm}$ holomorphic above/below $I$, continuous to $I$, equal there ⇒ the glued function is holomorphic |
| Ch. 2, Corollary 4.5 | Liouville's theorem |
| Ch. 3, Theorem 3.1 | Riemann's theorem on removable singularities (needs boundedness) |
| Ch. 3, Corollary 4.6 | $\sup_{\Omega}|f|\le\sup_{\partial\Omega}|f|$ for a region with compact closure |

No other result is invoked; the Poisson-kernel facts, the Plemelj/PV analysis, the endpoint
asymptotics and the counterexample are proved in the block.

## Three findings about the printed statement (all inside the block, in the remarks section)

1. **The jump identity holds on the open interval only.** At $x=\pm M$ the same computation gives
   $h(\pm M)/2$: half of the Poisson mass falls outside $[-M,M]$. (This is a property of the
   geometry, not a defect: at an endpoint the segment bounds the domain on one side only.)
2. **"Converge uniformly" in (b) can only mean uniformly on $[-M,M]$ when $h(\pm M)=0$.** For
   $h(M)\ne0$,
   $|g(M+i\epsilon)|=\frac{|h(M)|}{2\pi}\log\frac1\epsilon+O(1)$,
   so $g$ itself has no limit at the endpoints and (iii) fails there. The block proves the sharp
   dichotomy: the class $\mathcal{C}$ of functions satisfying (i)+(ii)+(iii) has **at most one**
   element, and $g\in\mathcal{C}$ iff $h(\pm M)=0$. If "supported in $[-M,M]$" is read as support
   inside the open interval — the reading under which the printed (b) is literally true — nothing
   is lost.
3. **The endpoint uniformity is not cosmetic.** Weaken (iii) to local uniform convergence on
   $(-M,M)$ — everything part (a) plus Hölder gives for $g$ — and uniqueness fails:
   $G=g+1/(z^2-M^2)$ satisfies (i), (ii) and that local form of (iii) with the same jump $h$, and
   $G\ne g$. The hint's "$g-G$ is entire" is exactly the endpoint hypothesis; the block supplies
   the missing steps (symmetry principle off $\{\pm M\}$, maximum modulus in the two half-discs,
   then Riemann).

## Numerical sanity checks (independent of the proof, run in this workspace)

$M=1$; $h=\cos(\pi x/2)$ (Hölder, $h(\pm1)=0$), $h\equiv1$, $h(x)=|x+\tfrac12|^{1/2}$
(Hölder, $\alpha=1/2$). Direct quadrature of $g$:

* jump at $x=0.3$: $g(x+i\epsilon)-g(x-i\epsilon)=0.8908890$ for $\epsilon=10^{-4}$ vs
  $h(0.3)=0.8910065$;
* Plemelj: $|g(0.3-i10^{-4})-(-h/2+A/(2\pi i))|=5.0\times10^{-5}$, decreasing like $O(\epsilon)$;
* endpoint jump: same difference at $x=1$ with $h\equiv1$ gives $0.49998$ → $h(1)/2$;
* endpoint growth: $|g(1+i\epsilon)|=1.472$ vs $\frac{1}{2\pi}\log\frac1\epsilon=1.466$ at
  $\epsilon=10^{-5}$, i.e. $\frac{|h|}{2\pi}\log\frac1\epsilon+O(1)$;
* uniformity: $\sup_{x\in[-0.98,0.98]}|g(x+i\epsilon)-g^{+}(x)|$ falls $1.1\times10^{-2}\to1.1\times10^{-4}$
  for $\epsilon=10^{-2}\to10^{-4}$ (Hölder $\alpha=1/2$: $9.6\times10^{-2}\to2.4\times10^{-3}$),
  and with $h(\pm1)=0$ the sup over $[-1,1]$ including the endpoints converges as well.

## Honest limits of this delivery

* The block proves the printed statement under the endpoint reading stated in it; it does not claim
  that the printed wording is correct without that reading — findings 1–3 above say where and why,
  with an explicit counterexample for the weaker reading.
* Whether the class $\mathcal{C}$ is *empty* when $h(\pm M)\ne0$ is not decided (the block proves
  only "at most one element"), and nothing in the solution depends on it.
* Only the printed problem was solved; no neighbouring problem of §9 was touched.
