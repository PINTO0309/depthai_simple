from abc import ABC, abstractmethod
from typing import List, Tuple
import os
from pathlib import Path

class AbstractReader(ABC):
    @abstractmethod
    def read(self):
        """
        Read a frame (or multiple frames) from the reader.
        @return: Single np.ndarray, or dict of frames and their names. None if frames weren't read or there was an error.
        """
        pass

    @abstractmethod
    def getStreams(self) -> List[str]:
        pass
 
    @abstractmethod
    def getShape(self, name: str) -> Tuple[int, int]:
        """
        Returns (width, height)
        """
        pass

    @abstractmethod
    def close(self):
        pass

    @abstractmethod
    def disableStream(self, name: str):
        """
        @param name: Name of the stream to be disabled
        """
        pass

    def _fileWithExt(self, folder: Path, ext: str) -> str:
        for f in os.listdir(str(folder)):
            if f.endswith(ext):
                return f
        raise ValueError(f"Couldn't find a file with '{ext}' extension in folder '{folder}'!")
