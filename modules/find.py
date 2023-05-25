import psutil

from typing import Union

class find:
    def process(process_id: Union[any, int]) -> dict[str]:
        """Get information about a process via its PID.

        Args:
            process_id (Union[any, int]): Process ID of the given application.

        Returns:
            dict[str]: Returns a dict containing information about the process.
        """
        try:
            process_result: object = psutil.Process(pid=process_id)
            
        except Exception as error:
            return {"error": error}