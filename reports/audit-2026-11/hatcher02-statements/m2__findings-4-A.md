# findings-4-A — SRC-TEXT-HAT02 §4.A (Basepoints and Homotopy)

Cards in section: **5** (E-HAT-4.A-1 … 5). Book exercise block: AT.txt **line 21092**
("Exercises"), statements at **21093–21129**.

## Per card

| id | statement | proof |
|---|---|---|
| E-HAT-4.A-1 | **statement matches** (AT 21093–21095). | unread |
| E-HAT-4.A-2 | **statement differs** — the final "In particular …" sentence is dropped (defect 1). | unread |
| E-HAT-4.A-3 | **statement matches** (AT 21102–21106). | unread |
| E-HAT-4.A-4 | **statement differs** — the bracketed identification of GL_n(Z) is dropped (defect 2). | unread |
| E-HAT-4.A-5 | **statement matches** (AT 21114–21129); "(a) … 2 dimensional" is hyphenated in the card, no change of content. | unread |

## Defects (most serious first)

1. **E-HAT-4.A-2: a printed consequence of the exercise is dropped.** Book, AT **21100–21101**:
   "Deduce a bijection of [X, K(π , 1)] with the set of orbits of Hom(π1 (X), π ) under composition
   with inner automorphisms of π . **In particular, if π is abelian then [X, K(π , 1)] = hX, K(π , 1)i
   = Hom(π1 (X), π ) .**"
   The card stops after "… inner automorphisms of π." The dropped sentence is the special case the
   section actually uses.
2. **E-HAT-4.A-4: bracketed hint dropped.** AT **21113**: "[ GLn (Z) is the automorphism group of
   Zn ≈ πk (∨n S k ) ≈ Hk (∨n S k ) .]"

## Census
5 cards; 2 of 5 statements differ. All 5 carry `source-checked` / `solution-written` /
`solution-reviewed` (`gpt-5.6-sol`).

## PROOF AUDIT

- **E-HAT-4.A-1 — proof correct.** F(z,t) = H(z,t)·γ(t)^{-1} with γ(t) = H(z_0,t) a loop at x_0 is
  continuous, has the right two time slices, and satisfies F(z_0,t) = x_0 for all t.
- **E-HAT-4.A-2 — proof correct.** A loop-action homotopy H from f to γf yields, on composing with
  a: S^n → X, a homotopy from fa to (γf)a whose basepoint traces γ, so [(γf)a] = β_γ[fa] for all a,
  i.e. (γf)_* = β_γ f_*; in degree 1 β_γ is conjugation by γ, and free homotopy classes are orbits,
  giving [X,K(π,1)] ≅ Hom(π1X,π)/Inn(π).
- **E-HAT-4.A-3 — proof correct.** Φ: Aut(K(π,1)) → Out(π) is well defined (changing the path
  changes by an inner automorphism); conversely [K,K] ≅ Hom(π,π)/Inn(π) and a map is a homotopy
  equivalence iff its endomorphism of π is an automorphism (a map inducing f_*^{-1} is an inverse
  because the composites induce the identity outer automorphism and hence are freely homotopic to the
  identity). Hence Aut(K(π,1)) ≅ Out(π).
- **E-HAT-4.A-4 — proof unread.**
- **E-HAT-4.A-5 — proof unread.**
