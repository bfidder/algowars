public class Task{

	private int task_id;
	private Integer processing_time;
	
	public int getTask_id() {
		return task_id;
	}
	public Integer getProcessing_time() {
		return processing_time;
	}
	public Integer getTaskId() {
		return task_id;
	}
	public Task(int task_id, int processing_time) {
		this.task_id = task_id;
		this.processing_time = processing_time;
	}
	public String toString() {
		return "Task id: " + task_id +", Procesing Time: " + processing_time;
	}
}
