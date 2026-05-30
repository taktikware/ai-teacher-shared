import os
from typing import List, Optional
from fastapi import HTTPException
import yaml

def validate_language(language: str):
    if language.lower() not in ["us", "uk"]:
        raise HTTPException(
            status_code=400,
            detail=f"'{language.lower()}' is not supported. Language must be 'us' or 'uk'."
        )

def validate_transcript(transcript: str):
    if not transcript:
        raise HTTPException(status_code=400, detail="Transcript cannot be empty.")

def validate_speed(speed: str):
    valid_speeds = ["very_slow", "slow", "medium", "fast", "very_fast"]
    if speed not in valid_speeds:
        raise HTTPException(
            status_code=400,
            detail=f"'{speed}' is not a valid speed. Choose from {', '.join(valid_speeds)}."
        )

# Get the directory where this file is located
_PACKAGE_DIR = os.path.dirname(os.path.abspath(__file__))
_MAP_DIR = os.path.join(_PACKAGE_DIR, "map")

with open(os.path.join(_MAP_DIR, "english_uk_mfa_valid_phones.yaml"), "r", encoding="utf-8") as f_uk:
    UK_VALID_PHONEMES = set(yaml.safe_load(f_uk))

with open(os.path.join(_MAP_DIR, "english_us_mfa_valid_phones.yaml"), "r", encoding="utf-8") as f_us:
    US_VALID_PHONEMES = set(yaml.safe_load(f_us))

def validate_dictionary(language: str, expected_size: int, dictionary: Optional[List[str]]):
    """
    Valida que un diccionario de fonemas IPA sea válido según el idioma especificado.
    
    Args:
        language (str): Idioma a validar ('us' o 'uk')
        expected_size (int): Número esperado de elementos en el diccionario
        dictionary (Optional[List[str]]): Lista de strings donde cada string contiene
            los fonemas para una palabra. Puede ser None, en cuyo caso se considera válido.
            
    Raises:
        HTTPException: Si el diccionario contiene fonemas inválidos o está vacío.
    """
    if dictionary is None:
        return  # Si es None, se considera válido
        
    if not dictionary:
        raise HTTPException(status_code=400, detail="Dictionary cannot be empty.")
    
    if len(dictionary) != expected_size:
        raise HTTPException(
            status_code=400,
            detail=f"The number of elements in the dictionary ({len(dictionary)}) does not match the expected size ({expected_size})."
        )
    
    # Seleccionar el conjunto de fonemas válidos según el idioma
    if language.lower() == "uk":
        valid_phonemes = UK_VALID_PHONEMES
    else:  # language es "us"
        valid_phonemes = US_VALID_PHONEMES
    
    # Validar que cada secuencia de fonemas en el diccionario sea válida
    for phoneme_sequence in dictionary:
        if not phoneme_sequence.strip():
            raise HTTPException(status_code=400, detail="Phoneme sequence cannot be empty.")
        
        # Validar que cada fonema individual sea un fonema IPA válido para el idioma especificado
        phonemes = phoneme_sequence.strip().split()
        for phoneme in phonemes:
            if phoneme not in valid_phonemes:
                raise HTTPException(
                    status_code=400,
                    detail=f"'{phoneme}' is not a valid IPA phoneme for {language.upper()} English. Valid IPA phonemes for {language.upper()} include: {', '.join(sorted(list(valid_phonemes)))}"
                )
