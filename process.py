from modules.find import find

class process_manager:
    def find_process_by_pid(process_id: int) -> dict[str]:
        return find.by_process_id(process_id)
    
    def find_process_by_name(process_name: str) -> dict[str]:
        return find.by_name(process_name)

if __name__ == "__main__":
    process_manager.find_process_by_name("test.exe")
    process_manager.find_process_by_pid(12345)