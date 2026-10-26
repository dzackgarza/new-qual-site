#!/usr/bin/env python3
"""Convert typed-step proofs to lamport_proof.lua filter syntax.

Reads a card with <N>M. typed steps and converts to ::: pf syntax.
"""
import re
import sys
from pathlib import Path


def parse_step_marker(line: str) -> tuple[int, int] | None:
    """Extract (level, number) from a line like '<1>2.'"""
    match = re.match(r'^(\s*)<(\d+)>(\d+)\.\s*$', line)
    if match:
        return (int(match.group(2)), int(match.group(3)))
    return None


def convert_proof(lines: list[str], start_idx: int) -> tuple[list[str], int]:
    """Convert one proof section starting at start_idx.
    
    Returns (converted_lines, next_idx_after_proof).
    """
    result = []
    i = start_idx
    
    # Collect all content until the closing :::
    proof_lines = []
    depth = 1
    i += 1  # Skip the opening ::: {.solution} or ::: {.proof}
    
    while i < len(lines) and depth > 0:
        if lines[i].strip().startswith(':::') and not lines[i].strip().startswith('::: '):
            # Check if it's an opener or closer
            if re.match(r'^:::\s*\{', lines[i]):
                depth += 1
            elif lines[i].strip() == ':::':
                depth -= 1
                if depth == 0:
                    break
        proof_lines.append(lines[i])
        i += 1
    
    # Now convert proof_lines
    converted = convert_typed_steps(proof_lines)
    
    result.append('::: pf\n')
    result.append('\n')
    result.extend(converted)
    result.append(':::\n')
    
    return result, i + 1  # Skip the closing :::


def convert_typed_steps(lines: list[str]) -> list[str]:
    """Convert lines containing typed steps to pf syntax."""
    result = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        step_info = parse_step_marker(line)
        
        if step_info:
            level, num = step_info
            # This is a step marker
            i += 1
            
            # Collect the claim (everything until ::: {.proof} or next step or Q.E.D.)
            claim_lines = []
            while i < len(lines):
                if parse_step_marker(lines[i]):
                    break
                if lines[i].strip().startswith('::: {.proof}') or lines[i].strip().startswith('::: proof'):
                    break
                if re.match(r'^<\d+>\d+\.\s+Q\.E\.D\.\s*$', lines[i]):
                    break
                claim_lines.append(lines[i])
                i += 1
            
            # Remove trailing blank lines from claim
            while claim_lines and not claim_lines[-1].strip():
                claim_lines.pop()
            
            # Check if this is Q.E.D.
            is_qed = (len(claim_lines) == 1 and 
                     claim_lines[0].strip() in ['Q.E.D.', 'Q.E.D'])
            
            if is_qed:
                # This is a Q.E.D. step
                result.append('::: pf-qed\n')
                result.append('\n')
                
                # Check for proof block
                if i < len(lines) and (lines[i].strip().startswith('::: {.proof}') or 
                                      lines[i].strip().startswith('::: proof')):
                    i += 1  # Skip proof opener
                    proof_lines = []
                    while i < len(lines) and lines[i].strip() != ':::':
                        proof_lines.append(lines[i])
                        i += 1
                    if i < len(lines):
                        i += 1  # Skip proof closer
                    
                    # Add proof content
                    for pline in proof_lines:
                        if pline.strip():
                            result.append(pline)
                    if proof_lines:
                        result.append('\n')
                
                result.append(':::\n')
                result.append('\n')
            else:
                # Regular step
                result.append('::: pf-step\n')
                result.append('\n')
                
                # Add claim
                for cline in claim_lines:
                    result.append(cline)
                if claim_lines:
                    result.append('\n')
                result.append('\n')
                
                # Check for proof block
                if i < len(lines) and (lines[i].strip().startswith('::: {.proof}') or 
                                      lines[i].strip().startswith('::: proof')):
                    i += 1  # Skip proof opener
                    result.append('::: pf-proof\n')
                    result.append('\n')
                    
                    proof_lines = []
                    while i < len(lines) and lines[i].strip() != ':::':
                        proof_lines.append(lines[i])
                        i += 1
                    if i < len(lines):
                        i += 1  # Skip proof closer
                    
                    # Recursively convert substeps in proof
                    converted_proof = convert_typed_steps(proof_lines)
                    result.extend(converted_proof)
                    
                    result.append(':::\n')
                    result.append('\n')
                
                result.append(':::\n')
                result.append('\n')
        else:
            # Not a step marker, keep as-is
            result.append(line)
            i += 1
    
    return result


def convert_file(filepath: Path) -> bool:
    """Convert one file. Returns True if converted, False if skipped."""
    content = filepath.read_text()
    lines = content.splitlines(keepends=True)
    
    # Find solution/proof sections with typed steps
    result = []
    i = 0
    converted = False
    
    while i < len(lines):
        line = lines[i]
        
        # Check if this is a solution/proof/hint section
        if (line.strip().startswith('::: {.solution}') or 
            line.strip().startswith('::: {.proof}') or
            line.strip().startswith('::: {.hint}')):
            
            # Check if it contains typed steps
            section_start = i
            section_lines = [line]
            depth = 1
            i += 1
            has_typed_steps = False
            
            while i < len(lines) and depth > 0:
                if lines[i].strip() == ':::':
                    depth -= 1
                    if depth == 0:
                        section_lines.append(lines[i])
                        i += 1
                        break
                elif lines[i].strip().startswith('::: {') or lines[i].strip().startswith('::: proof'):
                    depth += 1
                
                if parse_step_marker(lines[i]):
                    has_typed_steps = True
                
                section_lines.append(lines[i])
                i += 1
            
            if has_typed_steps:
                # Convert this section
                converted_section, _ = convert_proof(section_lines, 0)
                result.extend(converted_section)
                converted = True
            else:
                # Keep as-is
                result.extend(section_lines)
        else:
            result.append(line)
            i += 1
    
    if converted:
        filepath.write_text(''.join(result))
        return True
    return False


def main():
    if len(sys.argv) < 2:
        print("Usage: convert_lamport.py <file1> [file2 ...]")
        sys.exit(1)
    
    for filepath in sys.argv[1:]:
        path = Path(filepath)
        if path.exists():
            if convert_file(path):
                print(f"Converted: {filepath}")
            else:
                print(f"Skipped (no typed steps): {filepath}")
        else:
            print(f"Not found: {filepath}")


if __name__ == '__main__':
    main()
