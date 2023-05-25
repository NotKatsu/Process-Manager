import psutil

from typing import Union

class find:
    def by_process_id(process_id: Union[any, int]) -> dict[str]:
        """Get information about a process via its PID.

        Args:
            process_id (Union[any, int]): Process ID of the given application.

        Returns:
            dict[str]: Returns a dict containing information about the process.
        """
        try:
            process_result: object = psutil.Process(pid=process_id)
            
            process_information: dict[str] = {
                'name': process_result.name(),
                'status': process_result.status(),
                'memory_info': process_result.memory_info(),
                'cpu_percent': process_result.cpu_percent()    
            }
            
            return process_information
        except Exception as error:
            return {"error": error}