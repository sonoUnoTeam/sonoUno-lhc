#!/usr/bin/env python
 
from pathlib import Path

from sonouno_lhc.lhc_data import sonify_subject
from sonouno_lhc.io import extract_subjects

OUTPUT_PATH = Path('outputs')
OUTPUT_PATH.mkdir(exist_ok=True)


def sonify_subjects(path: Path) -> None:
    data = path.read_text().split('\n')
    for subject in extract_subjects(data):
        sound, fig = sonify_subject(subject)

        # Save the plot
        plot_path = OUTPUT_PATH / f'plot_dataset_{subject.id}.png'
        fig.savefig(plot_path, format='png')

        # Generate the wav file with the sonification
        sound_path = OUTPUT_PATH / f'sound_dataset_{subject.id}.wav'
        sound.to_wav(sound_path)


sonify_subjects(Path('sonification_reduced.txt'))
