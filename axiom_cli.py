#!/usr/bin/env python3
"""
AXIOM Core - Command Line Interface
Zero-dependency starter version
"""

from enum import Enum
from typing import List, Dict
import re

class AXIOMNode(str, Enum):
    INITIATION = "│"
    POTENTIAL = "¬"
    FLOW = "⌒"
    PROCESSING = "█"
    RAW_FORCE = "┼"
    IMPRINT = "┴"
    CONTAINMENT = "—"
    RECURRENCE = "┘"
    EMERGENCE = "┬"
    RETURN = "⌑"
    FOCUS = "◆"
    MANIFESTATION = "┌"
    DOMAIN = "└"
    EMISSION = "┐"
    GUIDANCE = "├"
    CONNECTION = "┤"
    SYNCHRONIZATION = "≡"
    IDENTITY = "⟦⟧"

class BasicAXIOMParser:
    def __init__(self):
        self.keyword_mappings = {
            AXIOMNode.FLOW: ['flow', 'transfer', 'move', 'current', 'propagate', 'travel'],
            AXIOMNode.PROCESSING: ['process', 'transform', 'compute', 'convert', 'calculate', 'change'],
            AXIOMNode.IMPRINT: ['store', 'remember', 'imprint', 'encode', 'memorize', 'save'],
            AXIOMNode.EMERGENCE: ['emerge', 'create', 'form', 'generate', 'arise', 'become'],
            AXIOMNode.CONTAINMENT: ['contain', 'bound', 'limit', 'restrict', 'constrain', 'within'],
            AXIOMNode.RECURRENCE: ['repeat', 'cycle', 'oscillate', 'recur', 'periodic', 'rhythm'],
            AXIOMNode.INITIATION: ['start', 'begin', 'initiate', 'source', 'origin'],
            AXIOMNode.IDENTITY: ['identity', 'self', 'essence', 'unique', 'distinct']
        }
    
    def parse_text(self, text: str) -> List[AXIOMNode]:
        symbols = []
        text_lower = text.lower()
        
        for symbol, keywords in self.keyword_mappings.items():
            if any(keyword in text_lower for keyword in keywords):
                symbols.append(symbol)
                
        return self._apply_natural_flow(symbols)
    
    def _apply_natural_flow(self, symbols: List[AXIOMNode]) -> List[AXIOMNode]:
        natural_order = [
            AXIOMNode.INITIATION, AXIOMNode.FLOW, AXIOMNode.PROCESSING,
            AXIOMNode.IMPRINT, AXIOMNode.EMERGENCE, AXIOMNode.CONTAINMENT,
            AXIOMNode.RECURRENCE
        ]
        
        ordered_symbols = [s for s in natural_order if s in symbols]
        remaining_symbols = [s for s in symbols if s not in natural_order]
        
        return ordered_symbols + remaining_symbols

class STICalculator:
    def __init__(self):
        self.nsf_weights = {
            AXIOMNode.INITIATION: 1.0,
            AXIOMNode.FLOW: 1.2, 
            AXIOMNode.PROCESSING: 1.5,
            AXIOMNode.IMPRINT: 1.1,
            AXIOMNode.EMERGENCE: 1.4,
            AXIOMNode.CONTAINMENT: 1.0,
            AXIOMNode.RECURRENCE: 1.1,
            AXIOMNode.RETURN: 1.0
        }
        
        self.nsf_core_nodes = list(self.nsf_weights.keys())
    
    def calculate_sti(self, symbols: List[AXIOMNode]) -> Dict:
        present_nodes = [s for s in symbols if s in self.nsf_core_nodes]
        missing_nodes = [s for s in self.nsf_core_nodes if s not in symbols]
        
        total_weight = sum(self.nsf_weights.values())
        missing_weight = sum(self.nsf_weights[node] for node in missing_nodes)
        
        sti_score = 1 - (missing_weight / total_weight)
        
        return {
            'symbols': symbols,
            'missing_nodes': missing_nodes,
            'sti_score': round(sti_score, 3),
            'present_nodes': present_nodes
        }

def main():
    parser = BasicAXIOMParser()
    calculator = STICalculator()
    
    print("🌌 AXIOM Structural Analysis CLI")
    print("=" * 40)
    
    while True:
        text = input("\n📝 Enter system description (or 'quit'): ")
        
        if text.lower() == 'quit':
            break
            
        symbols = parser.parse_text(text)
        result = calculator.calculate_sti(symbols)
        
        print(f"\n🔍 Found Symbols: {''.join(result['symbols'])}")
        print(f"📊 STI Score: {result['sti_score']}")
        
        if result['missing_nodes']:
            print(f"⚠️  Missing: {', '.join(result['missing_nodes'])}")
        else:
            print("✅ Structurally complete!")
            
        print("-" * 40)

if __name__ == "__main__":
    main()
